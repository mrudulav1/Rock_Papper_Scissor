from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.game_view, name='game'),
    path('result/', views.result_view, name='result'),
    path('play-again/', views.play_again_view, name='play_again'),
]
