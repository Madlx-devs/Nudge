from django.shortcuts import render
from .models import nudge
# Create your views here.
def notifications(request):
    return render(request , 'nudge/notifications.html' )
def home(request):
    return render(request , 'nudge/home.html')

def allnudges(request):
    Nudge = nudge.objects.all()
    return render(request ,'nudge/allnudges.html',{'Nudge': Nudge})