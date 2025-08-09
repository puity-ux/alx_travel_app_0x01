from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings_list, name='listings-list'),
    path('<int:pk>/', views.listing_detail, name='listing-detail'),
]
