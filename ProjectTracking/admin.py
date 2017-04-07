from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ProjectTracking.models import Requirement, Employee


class RequirementAdmin(admin.ModelAdmin):
    # fields = ['r_info_name',
    #           'r_info_submit_time',
    #           'r_info_submit_employee',
    #           'r_info_value',
    #           ]
    list_display = ('r_info_name',
                    'r_info_submit_time',
                    # 'r_info_submit_employee',
                    'r_info_submit_department',
                    'r_info_submit_person',
                    'r_info_value',
                    )

    @staticmethod
    def r_info_submit_person(obj):
        return obj.r_info_submit_employee.employee.person

    @staticmethod
    def r_info_submit_department(obj):
        return obj.r_info_submit_employee.employee.get_department_display()


admin.site.register(Requirement, RequirementAdmin)


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class EmployeeAdmin(UserAdmin):
    inlines = (EmployeeInline, )
    list_display = ('username', 'person', 'department', 'is_staff',)

    @staticmethod
    def person(obj):
        return obj.employee.person

    @staticmethod
    def department(obj):
        return obj.employee.get_department_display()


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
