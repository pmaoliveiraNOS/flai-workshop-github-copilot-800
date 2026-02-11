from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fitness team',
            created_at=datetime.now()
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness warriors',
            created_at=datetime.now()
        )

        # Create users - Marvel heroes
        self.stdout.write('Creating Marvel heroes...')
        marvel_users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com'},
            {'name': 'Steve Rogers', 'email': 'captain.america@marvel.com'},
            {'name': 'Thor Odinson', 'email': 'thor@asgard.marvel.com'},
            {'name': 'Natasha Romanoff', 'email': 'black.widow@marvel.com'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com'},
        ]

        # Create users - DC heroes
        self.stdout.write('Creating DC heroes...')
        dc_users = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com'},
        ]

        created_users = []

        for user_data in marvel_users:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team_id=str(team_marvel._id),
                created_at=datetime.now()
            )
            created_users.append(user)

        for user_data in dc_users:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team_id=str(team_dc._id),
                created_at=datetime.now()
            )
            created_users.append(user)

        # Create workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity military-style workout inspired by Captain America',
                'category': 'Strength',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_per_session': 500
            },
            {
                'name': 'Web-Slinger Cardio',
                'description': 'Agility and cardio training like Spider-Man',
                'category': 'Cardio',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_per_session': 400
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Combat training inspired by Wonder Woman',
                'category': 'Combat',
                'difficulty': 'Hard',
                'duration': 55,
                'calories_per_session': 550
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Ultra-fast interval running like The Flash',
                'category': 'Cardio',
                'difficulty': 'Hard',
                'duration': 30,
                'calories_per_session': 450
            },
            {
                'name': 'Gotham Detective Patrol',
                'description': 'Stealth and endurance training like Batman',
                'category': 'Endurance',
                'difficulty': 'Medium',
                'duration': 50,
                'calories_per_session': 380
            },
            {
                'name': 'Asgardian Power Lift',
                'description': 'Heavy lifting workout worthy of Thor',
                'category': 'Strength',
                'difficulty': 'Hard',
                'duration': 40,
                'calories_per_session': 420
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Aquatic workout inspired by Aquaman',
                'category': 'Swimming',
                'difficulty': 'Medium',
                'duration': 45,
                'calories_per_session': 350
            },
            {
                'name': 'Yoga with the Sorcerer Supreme',
                'description': 'Flexibility and mindfulness training',
                'category': 'Flexibility',
                'difficulty': 'Easy',
                'duration': 30,
                'calories_per_session': 150
            },
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        # Create activities
        self.stdout.write('Creating activity logs...')
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Yoga', 'Boxing', 'HIIT', 'Climbing']
        
        for user in created_users:
            num_activities = random.randint(5, 15)
            total_calories = 0
            
            for i in range(num_activities):
                duration = random.randint(20, 90)
                calories = duration * random.randint(5, 10)
                total_calories += calories
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=random.choice(activity_types),
                    duration=duration,
                    calories=calories,
                    date=datetime.now() - timedelta(days=random.randint(0, 30)),
                    notes=f'Great workout session!'
                )
            
            # Create leaderboard entry
            Leaderboard.objects.create(
                user_id=str(user._id),
                team_id=user.team_id,
                total_calories=total_calories,
                total_activities=num_activities,
                rank=0,  # Will be calculated
                updated_at=datetime.now()
            )

        # Calculate and update ranks
        self.stdout.write('Calculating leaderboard ranks...')
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()

        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        try:
            db.users.create_index([('email', 1)], unique=True)
            self.stdout.write(self.style.SUCCESS('Unique index created on email field'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Index might already exist: {e}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDatabase populated successfully!\n'
            f'Teams: {Team.objects.count()}\n'
            f'Users: {User.objects.count()}\n'
            f'Activities: {Activity.objects.count()}\n'
            f'Leaderboard entries: {Leaderboard.objects.count()}\n'
            f'Workouts: {Workout.objects.count()}'
        ))
