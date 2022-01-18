from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),

    path('publish-a-new-product/', views.PublishProduct, name="PublishProduct"),

    path('<str:product>', views.product),
]
