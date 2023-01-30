from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs) : 
    homecontext = {
        "mytext" : "homepage" ,
        "mynumber" : 8 ,
        "mylist" : [1,4,2]
    }
    print(request.user)
    return render(request, "home.html" , homecontext )  #html encoded string 
    # return render(request, "home.html" , {})

def contact_view(request, *args, **kwargs) : 
    print(request.user)
    return render(request, "contact.html" , {})

# Create your views here.
