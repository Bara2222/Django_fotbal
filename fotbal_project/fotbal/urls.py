from django.urls import path
from . import views

app_name = 'fotbal'

urlpatterns = [
    path('', views.home, name='home'),  # tato cesta pro domovskou stránku
    path('tymy/', views.teams, name='teams'),
    path('tymy/<int:pk>/', views.team_detail, name='team_detail'),
    path('hraci/', views.players, name='players'),
    path('hraci/<int:pk>/', views.player_detail, name='player_detail'),
    path('zapasy/', views.matches, name='matches'),
    path('zapasy/<int:pk>/', views.match_detail, name='match_detail'),
]
