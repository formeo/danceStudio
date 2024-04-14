
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Company,Courses,Costs



class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class CostsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost_date', 'cost')
    list_filter = (
        ('cost_date', DateFieldListFilter),
    )


admin.site.register(Company, CompanyAdmin)

admin.site.register(Courses, CoursesAdmin)

admin.site.register(Costs, CostsAdmin)
