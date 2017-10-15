from django.shortcuts import render

# Create your views here.

def index(request):

     #defining a variable
     number = 6
     thing = "Thing name"   
     #passing the var into our view!
     return render(request, 'index.html', {
         'number': number,
         'thing': thing,
    })
