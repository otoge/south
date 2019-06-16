from django.urls import path
from .views import home_page, ItemDetailView, ItemFilterView, MyView



urlpatterns = [
    path("", ItemFilterView.as_view(), name="home"),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('user', MyView.as_view(), name='user'),
]