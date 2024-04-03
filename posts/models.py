from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from extentions.utils import jalali_converted

#post Manager
class PostManager(models.Manager):
     def publish(self):
         return self.filter(is_enable = True)

#category Manager
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status = True)

#Models Category
class CategoryModel(models.Model):
    parent = models.ForeignKey('self',default = None,null = True , blank = True , on_delete = models.SET_NULL,verbose_name = 'زیر دسته',related_name = 'child')
    title = models.CharField(max_length=50, verbose_name = ' عنوان دسته بندی')
    status = models.BooleanField(default = True ,verbose_name = 'نمایش داده شود')
    slug= models.SlugField(max_length = 50, unique=True,verbose_name = 'کلمه کلیدی')
    position = models.IntegerField(verbose_name = "موقعیت")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position']
    
    def __str__(self):
        return "{}".format(self.title)
    
    objects = CategoryManager()
    

#Models Post
class PostModel(models.Model):
    title = models.CharField(max_length=50,help_text='Insert Name Post',verbose_name = 'عنوان')
    description= models.TextField(verbose_name = 'شرح عنوان')
    slug= models.SlugField(max_length = 50, unique=True,verbose_name = 'کلمه کلیدی')
    category = models.ManyToManyField(CategoryModel,verbose_name= " دسته بندی",related_name='postmodel')
    thumbnail = models.ImageField(upload_to = 'images/',verbose_name='تصویر' )
    is_enable = models.BooleanField(default=False,verbose_name = 'فعالیت')
    publish = models.DateTimeField(default = timezone.now , verbose_name = 'زمان تولید')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = ' پست ها'

    def __str__(self):
        return '{}-{}'.format(self.id , self.title)
    
    def jpublish(self):
        return jalali_converted(self.publish)
    jpublish.short_description = "زمان انتشار"

    def thumbnail_tag(self):
        return format_html("<img scr = '{}'>".format(self.thumbnail))
    thumbnail_tag.short_description = "عکس"

    def published(self):
        return self.category.filter(status = True)

    objects = PostManager()

