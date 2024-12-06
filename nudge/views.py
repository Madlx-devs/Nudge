from django.shortcuts import render
# Create your views here.
def notifications(request):
    return render(request , 'nudge/notifications.html' )
def home(request):
    return render(request , 'nudge/home.html')