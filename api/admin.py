from django.contrib import admin
from api.models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type', 'added', 'active')


admin.site.register(Company)
admin.site.register(Employee)