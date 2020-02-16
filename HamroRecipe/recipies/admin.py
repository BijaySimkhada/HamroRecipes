from django.contrib import admin
from .models import Recipe, Incredients, Step

class RecipeAdmin(admin.ModelAdmin):

    list_display = ('r_name','video','username','seen','category','type','img','created_at')

# Register your models here.


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Incredients)
admin.site.register(Step)
