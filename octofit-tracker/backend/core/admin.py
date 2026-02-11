from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team_id', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'user_id', 'duration', 'calories', 'date')
    search_fields = ('activity_type', 'user_id')
    list_filter = ('activity_type', 'date')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'team_id', 'rank', 'total_calories', 'total_activities', 'updated_at')
    search_fields = ('user_id', 'team_id')
    list_filter = ('rank', 'updated_at')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'duration', 'calories_per_session')
    search_fields = ('name', 'category')
    list_filter = ('category', 'difficulty')
