from django.shortcuts import render
from collection.models import Thing


def index(request):

    things = Thing.objects.all()
    #return items with new in the name 
   #things = Thing.objects.filter(name__contains='new')
    # random order
 #   things = Thing.objects.all().order_by('?')
    return render(request, 'index.html', {
         'things': things,
    })

# new view!!
def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
        })
