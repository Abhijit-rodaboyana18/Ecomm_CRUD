from django.urls import path
from ecomm_app import views

urlpatterns = [
    path('/home',views.home,name='home'),
    path('/delete/<int:id>', views.delete, name='delete'),
    path('/update/<int:id>', views.update, name='update'),
    path('/success', views.success, name='success'),
]