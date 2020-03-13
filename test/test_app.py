import pytest
from fitapp.tmb import ComputeDailyDiet


def test_app_gain():
    app = ComputeDailyDiet()
    goal, kcal = app.compute_tmb(100, 180, 30, 'gain')
    assert str(goal) == 'Gain'


def test_app_lose():
    app = ComputeDailyDiet()
    goal, kcal = app.compute_tmb(100, 180, 30, 'lose')
    assert str(goal) == 'Lose'


def test_app_maintain():
    app = ComputeDailyDiet()
    goal, kcal = app.compute_tmb(100, 180, 30, 'maintain')
    assert str(goal) == 'Maintain'
