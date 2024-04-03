from django.contrib import admin
from .models import PostModel,CategoryModel
from django.utils.translation import ngettext


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent','title','position' ,'slug','status')
    list_filter = ['status',]
    search_fields = ['title',]
    ordering = ['position',]

admin.site.register(CategoryModel,CategoryAdmin)

@admin.action(description="فعال")
def make_is_enable(modeladmin, request, queryset):
    updated = queryset.update(is_enable="True")
    modeladmin.message_user(request,ngettext(
                "%d پست فعال شد",
                "%d تا پست فعال شدند",
                updated,
            )
            % updated,
        )
        

@admin.action(description="غیرفعال")
def make_is_unable(modeladmin, request, queryset):
    updated = queryset.update(is_enable="False")
    modeladmin.message_user(request,ngettext(
                "%d پست غیر شد",
                "%d تا پست غیر فعال شدند",
                updated,
            )
            % updated,
        )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title' ,'thumbnail_tag', 'is_enable' , 'jpublish' ,'category_to_str' )
    list_filter = ['is_enable',]
    search_fields = ['title','description']
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['id',]
    actions = [make_is_enable , make_is_unable]

    def category_to_str(self , obj):
        return ", ".join([CategoryAdmin.title for CategoryAdmin in obj.category.all()])
    category_to_str.short_description="دسته بندی"
    
admin.site.register(PostModel,PostAdmin)