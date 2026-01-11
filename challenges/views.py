from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
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
months = list(monthly_challenges.keys())

# Create your views here.


def monthly_challenge_by_number(request, month):
    if month > len(months):
        return HttpResponse("Invalid month number.")

    month_name = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{month_name}")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")