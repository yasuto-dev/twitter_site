from django.urls import path

from .views import IndexView, PostCreateView ,PostDetailView,PostDeleteView
from . import views
app_name = "app"

urlpatterns = [
    path("",IndexView.as_view(),name= "index"),
    path("post_create/",PostCreateView.as_view(),name="post-create"),
    path('post_detail/<int:pk>/', PostDetailView.as_view(),name = "post-detail"),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(),name = "post-delete"),
]
