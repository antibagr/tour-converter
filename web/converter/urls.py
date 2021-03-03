from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.upload_tour, name='main'),
    # path('converter/?P<str:', views.convert_tour, name='convert-tour'),
]
