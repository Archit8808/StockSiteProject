from django import forms 

from .models import Services 



class ServiceForm(forms.ModelForm) : 
    class Meta : 
        model = Services 
        fields = [ 
            'title' ,
            'description', 
            'price'
        ]

class RawServiceForm(forms.Form) :
    title = forms.CharField() 
    description = forms.CharField(required = False , widget = forms.Textarea(attrs = {
        "class" :"new-class-name two" ,
        "rows" : 100,
        "cols" : 120}
    )
    ) 
    price = forms.DecimalField() 