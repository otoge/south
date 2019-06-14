from django.urls import path
from .views import home_page, ItemDetailView, ItemFilterView


urlpatterns = [
    path("", ItemFilterView.as_view(), name="home"),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
]