from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.temphome, name="home"),
    path('become-a-retailer/', views.becomeRetailer, name="becomeRetailer"),
    path('welcome-retailer', views.retailerWelcome, name="retailerWelcome"),
    path('profile/', views.UserProfile, name="UserProfile"),
    path('logout/', views.logoutPath, name="logoutPath")
]
