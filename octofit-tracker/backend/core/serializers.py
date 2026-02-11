from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'team', 'team_id', 'created_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_username(self, obj):
        """Return the name as username"""
        return obj.name
    
    def get_first_name(self, obj):
        """Split name into first name"""
        name_parts = obj.name.split(' ', 1)
        return name_parts[0] if name_parts else ''
    
    def get_last_name(self, obj):
        """Split name into last name"""
        name_parts = obj.name.split(' ', 1)
        return name_parts[1] if len(name_parts) > 1 else ''
    
    def get_team(self, obj):
        """Get team name from team_id"""
        if obj.team_id:
            try:
                team = Team.objects.get(_id=ObjectId(obj.team_id))
                return team.name
            except (Team.DoesNotExist, Exception):
                return None
        return None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members_count']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_members_count(self, obj):
        """Count the number of users in this team"""
        return User.objects.filter(team_id=str(obj._id)).count()


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    calories_burned = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'user', 'activity_type', 'duration', 'distance', 'calories', 'calories_burned', 'date', 'notes']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user(self, obj):
        """Get user name from user_id"""
        if obj.user_id:
            try:
                user = User.objects.get(_id=ObjectId(obj.user_id))
                return user.name
            except (User.DoesNotExist, Exception):
                return None
        return None
    
    def get_distance(self, obj):
        """Return 0 as default distance (not in model)"""
        return 0
    
    def get_calories_burned(self, obj):
        """Map calories field to calories_burned"""
        return obj.calories


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    total_points = serializers.SerializerMethodField()
    activities_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user', 'team_id', 'team', 'total_calories', 'total_points', 'total_activities', 'activities_count', 'rank', 'updated_at']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user(self, obj):
        """Get user name from user_id"""
        if obj.user_id:
            try:
                user = User.objects.get(_id=ObjectId(obj.user_id))
                return user.name
            except (User.DoesNotExist, Exception):
                return None
        return None
    
    def get_team(self, obj):
        """Get team name from team_id"""
        if obj.team_id:
            try:
                team = Team.objects.get(_id=ObjectId(obj.team_id))
                return team.name
            except (Team.DoesNotExist, Exception):
                return None
        return None
    
    def get_total_points(self, obj):
        """Map total_calories to total_points"""
        return obj.total_calories
    
    def get_activities_count(self, obj):
        """Map total_activities to activities_count"""
        return obj.total_activities


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    workout_type = serializers.SerializerMethodField()
    difficulty_level = serializers.SerializerMethodField()
    calories_estimate = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'category', 'workout_type', 'difficulty', 'difficulty_level', 'duration', 'calories_per_session', 'calories_estimate']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_workout_type(self, obj):
        """Map category to workout_type"""
        return obj.category
    
    def get_difficulty_level(self, obj):
        """Map difficulty to difficulty_level"""
        return obj.difficulty
    
    def get_calories_estimate(self, obj):
        """Map calories_per_session to calories_estimate"""
        return obj.calories_per_session
