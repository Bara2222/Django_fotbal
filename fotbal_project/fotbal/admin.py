from django.contrib import admin
from .models import Team, Player, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'position', 'age', 'nationality')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'away_team', 'home_goals', 'away_goals')
