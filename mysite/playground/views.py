from django.shortcuts import render
from django.http import HttpResponse
from .models import Services

from .forms import ServiceForm,RawServiceForm



def say_hello(request) : 
    return HttpResponse('Hello User')




    
def service_create_view(request) : 
    my_form = RawServiceForm()
    if request.method == "POST" :  
        my_form = RawServiceForm(request.POST)
        if my_form.is_valid() : 
            my_new_title = request.POST.get('title')
            print(my_form.cleaned_data)
            Services.objects.create(title = my_new_title) 
   
    servicecontext = {
        'form' : my_form 
    }

    return render(request, "service/servicecreate.html" , servicecontext)

def service_detail_view(request) : 
    obj = Services.objects.get(id=1)
    servicecontext = {
        'title' : obj.title , 
        'description' : obj.description, 
        'price' : obj.price 
    }

    return render(request, "service/detail.html" , servicecontext)

# Create your views here.


def dynamic_lookup_view(request,my_id) : 
    obj = Services.objects.get(id=my_id) 
    context = {
        'object' : obj 

    }
    return render(request, "service/detail.html" , context)

def stock_search_view(request) : 
    context ={}
   
    return render(request, "service/stocksearch.html" , context)





 



