from django.urls import path
from basicforms import views
from django.contrib import admin

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^admin/', admin.site.urls),
    path(r'^add/', views.form_view, name='form_name'),
]
