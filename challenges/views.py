from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

    
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    if month > len(months):
        return HttpResponse("Invalid month number.")

    month_name = months[month - 1]
    redirect_url = reverse("month-challenge", args=[month_name])
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{month.capitalize()}</h1><p>{challenge_text}</p>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported.")
