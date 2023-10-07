from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.log_in),
    path('logout/', views.log_out,name='logout'),
    path('',views.Home_page)
]