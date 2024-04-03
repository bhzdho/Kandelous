from django.urls import path
from .views import post_detail,Post_Listview,post_category

app_name='posts'
urlpatterns = [
    path('',Post_Listview.as_view() , name='index'),
    path('page/<int:page>',Post_Listview.as_view() , name='index'),
    path('home/<int:id>',post_detail , name='detail'),
    path('category/<slug:slug>',post_category , name='category'),
    path('category/<slug:slug>/page/<int:page>',post_category , name='category'),
]