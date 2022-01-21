from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cats/<int:car_id>/add_fueling/', views.add_fueling, name='add_fueling'),
    path('paint/', views.PaintList.as_view(), name='paint_index'),
    path('paint/<int:pk>/', views.PaintDetail.as_view(), name='paint_detail'),
    path('paint/create/', views.PaintCreate.as_view(), name='paint_create'),
    path('paint/<int:pk>/update/', views.PaintUpdate.as_view(), name='paint_update'),
    path('paint/<int:pk>/delete/', views.PaintDelete.as_view(), name='paint_delete'),
]