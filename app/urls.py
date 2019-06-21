from django.urls import path
from .views import home_page, ItemDetailView, ItemFilterView, MyView, ajax_post_add, PostList
from django.conf.urls import include, url


app_name = "app"


urlpatterns = [
    path("", ItemFilterView.as_view(), name="home"),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('user', MyView.as_view(), name='user'),
    path("ajax/", ajax_post_add, name="ajax_post_add"),
    path("ajax_test/", PostList.as_view(), name="ajax_test"),
]