from django.contrib import admin
from . import models

class VictimAdmin(admin.ModelAdmin):
    list_display = ('id','ip','code')

admin.site.register(models.Victim,VictimAdmin)
