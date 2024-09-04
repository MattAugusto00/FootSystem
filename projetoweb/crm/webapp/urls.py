from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name=""),
  path('register', views.register, name="register"),
  path('my-login', views.my_login, name="my-login"),
  path('user-logout', views.user_logout, name="user-logout"),

  # CRUD
  path('dashboard', views.dashboard, name="dashboard"),
  path('create-transfer', views.create_transfer, name="create-transfer"),
  path('update-transfer/<int:pk>', views.update_transfer, name="update-transfer"),
  path('transfer/<int:pk>', views.singular_transfer, name="transfer"),
  path('delete-transfer/<int:pk>', views.delete_transfer, name="delete-transfer"),
]