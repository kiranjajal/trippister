from django.contrib import admin
from django.urls import path
from .import views

app_name = 'accounts'
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('signin/',views.register,name="register"),
]