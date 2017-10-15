from django.contrib import admin

# importing the model
from collection.models import Thing

# setting up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}



# register the model
admin.site.register(Thing, ThingAdmin)
