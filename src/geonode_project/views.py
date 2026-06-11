from django.conf import settings
from django.shortcuts import render
import requests



def my_custom_view(request):
    """
    This is the custom view takes care how showing our nice view

    attribute:
        - request (Request Object): is the request that the user send via browser and the fuction needs to handle
    
    return:
        - HttpResponse (HttpResponse): is the response that the function will use to render my string
    """
    # https://jsonplaceholder.typicode.com/posts/1/comments

    url = settings.API_URL

    my_response = requests.get(url)

    #for element in my_response.json():
    #    print(element)

    return render(request, "geonode_project/my_custom_view.html", {"data": my_response.json()})