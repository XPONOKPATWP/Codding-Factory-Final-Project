from django.contrib import admin

from GeoApp.models import UserQueryLogs


# Register your models here.

class QueryAdmin(admin.ModelAdmin):
    list_display = ['username', 'query_city_1', 'query_city_2', 'fuel_consumption', 'calculated_distance']


admin.site.register(UserQueryLogs, QueryAdmin)
