from django.contrib import admin
from .models import Recipe, Incredients, Step
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Incredients)
admin.site.register(Step)