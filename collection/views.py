from django.shortcuts import render

# Create your views here.

def index(request):
        #this is your brand damn new view
        return render(request, 'index.html')
