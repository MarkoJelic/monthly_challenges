from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month):
    challenges = {
        "january": "Eat no meat for the entire month!",
        "february": "Walk 20 minutes every day!",
        "march": "Learn Django for at least 20 minutes every day!",
        "april": "Read a new book each week!",
        "may": "Practice meditation daily!",
        "june": "Write in a journal every night!",
        "july": "Take a photo every day!",
        "august": "Try a new recipe each week!",
        "september": "Go for a run three times a week!",
        "october": "Learn a new language for 15 minutes daily!",
        "november": "Volunteer for a local charity!",
        "december": "Reflect on the year and set goals for the next!"
    }

    challenge_text = challenges.get(month, "This month is not supported.")
    return HttpResponse(challenge_text)