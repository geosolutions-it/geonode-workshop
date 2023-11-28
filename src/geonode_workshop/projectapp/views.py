from django.shortcuts import render

# Create your views here.

def workshop_view(request, *args, **kwargs):
    return render(request, "workshop.html")
