from django.core.paginator import Paginator
from django.shortcuts import render ,get_object_or_404 
from .models import PostModel,CategoryModel
from django.views.generic import ListView,DetailView

class Post_Listview(ListView):
    model = PostModel
    paginate_by = 3
    template_name = "posts/index.html"

    def get_context_data(self, **kwargs):
        post_get = PostModel.objects.publish()
        context = super().get_context_data(**kwargs)
        context['post_get'] = post_get
        return context

# def post_render(request,page=1):
#     post_objects = PostModel.objects.publish()
#     paginator=Paginator(post_objects,3)
#     post_get = paginator.get_page(page)
#     context={
#           "post_get":post_get,
#         }
#     return render(request,"posts/index.html",context=context)
    
# class Post_Detail_Listview(DetailView):
#     model = PostModel
#     template_name = 'posts/post.html'

#     def get_context_data(self ,id,**kwargs):
#         detail = PostModel.objects.get(id=id)
#         context = super().get_context_data(**kwargs)
#         context['detail'] = detail
#         return context

def post_detail(request,id):
    context = {
        "detail":get_object_or_404(PostModel,id=id),
    }
    return render(request,'posts/post.html',context=context)

def post_category(request,slug,page=1):
    category = get_object_or_404(CategoryModel,slug=slug)
    post_list = category.postmodel.all()
    paginator = Paginator(post_list,2)
    post_get = paginator.get_page(page)
    context = {
        "category" : category,
        "post_get" : post_get
    }
    return render(request,'posts/category.html',context=context)