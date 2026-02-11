#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from core.models import Leaderboard, User, Team
from bson import ObjectId

# Get first leaderboard entry
entry = Leaderboard.objects.first()
print(f'Leaderboard entry:')
print(f'  user_id: {entry.user_id} (type: {type(entry.user_id)})')
print(f'  team_id: {entry.team_id} (type: {type(entry.team_id)})')

# Test user lookup
print(f'\nTesting User lookup:')
try:
    user = User.objects.get(_id=entry.user_id)
    print(f'  Direct string lookup: SUCCESS - {user.name}')
except Exception as e:
    print(f'  Direct string lookup: FAILED - {e}')

try:
    user = User.objects.get(_id=ObjectId(entry.user_id))
    print(f'  ObjectId lookup: SUCCESS - {user.name}')
except Exception as e:
    print(f'  ObjectId lookup: FAILED - {e}')

# Test team lookup
print(f'\nTesting Team lookup:')
try:
    team = Team.objects.get(_id=entry.team_id)
    print(f'  Direct string lookup: SUCCESS - {team.name}')
except Exception as e:
    print(f'  Direct string lookup: FAILED - {e}')

try:
    team = Team.objects.get(_id=ObjectId(entry.team_id))
    print(f'  ObjectId lookup: SUCCESS - {team.name}')
except Exception as e:
    print(f'  ObjectId lookup: FAILED - {e}')
