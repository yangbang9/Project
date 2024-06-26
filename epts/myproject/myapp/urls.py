from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('find_similar_player/', views.find_similar_player, name='find_similar_player'),
    path('input_info/', views.input_info, name='input_info'),
    path('compare_players/', views.compare_players, name='compare_players'),
    path('compare_result/', views.compare_result, name='compare_result'),
    
    
]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)