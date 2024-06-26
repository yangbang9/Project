from django.urls import path, include
from . import views

app_name = "background_setting"

urlpatterns = [
    path('', views.index, name='index'),
    path('back_setting/', views.back_setting, name='back_setting'),
    path('best11/', views.best11, name='best11'),
    path('ranking/', views.ranking, name='ranking'),
    path('international/', views.international, name='international'),
]