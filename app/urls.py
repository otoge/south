from django.urls import path
from .views import home_page, ItemDetailView


urlpatterns = [
    path("", home_page, name="home"),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
]