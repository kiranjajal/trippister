from django.contrib import admin
from django.urls import path
from . import views

app_name="home"
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('overview',views.over,name="over"),
    path('itinerary',views.itin,name="itin"),
    path('location',views.loc,name="loc"),
    path('reviews', views.rev, name="rev"),
]
