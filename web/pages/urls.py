from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main_page, name='pages-main'),
    path('home/', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'),
    path('password/', views.change_password, ),
    # re_path(r'^.*/$', views.not_found, name='redirect-home'),
]
