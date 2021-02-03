from django.contrib import admin

# Register your models here.
from api.models import Film, AdditionalInfo, Review, Actor

admin.site.register(Film)
admin.site.register(AdditionalInfo)
admin.site.register(Review)
admin.site.register(Actor)
