from transfersapp import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('clubes/', views.clubes, name='listagem_clubes'),
    path('admin/', admin.site.urls),
]