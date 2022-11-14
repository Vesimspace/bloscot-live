from django.urls import path
from .views import BlogPageView, BlogDetailView, BlogOtherView

urlpatterns = [

    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('', BlogPageView.as_view(), name='index'),
    path('blog/', BlogOtherView.as_view(), name='blog'),
    ]