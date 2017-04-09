from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ProjectTracking.models import Requirement, Employee


class RequirementAdmin(admin.ModelAdmin):
    model = Requirement
    fieldsets = [
        ('需求基本信息', {'fields': ['i_name',
                               'i_submit_time',
                               'i_submit_user',
                               'i_value',
                               'i_file']}),
        ('需求管理相关信息与状态', {'fields': ['r_category']}),
        # ('项目管理相关信息与状态', {'fields': ['']}),
    ]

    list_display = ('i_name',
                    'i_submit_time',
                    'i_submit_department',
                    'i_submit_person',
                    'i_value',
                    )

    @staticmethod
    def i_submit_person(obj):
        return obj.i_submit_user.employee.person

    @staticmethod
    def i_submit_department(obj):
        return obj.i_submit_user.employee.get_department_display()


admin.site.register(Requirement, RequirementAdmin)


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class EmployeeAdmin(UserAdmin):
    inlines = (EmployeeInline, )
    list_display = ('username', 'person', 'department', 'is_staff', 'is_active')

    @staticmethod
    def person(obj):
        return obj.employee.person

    @staticmethod
    def department(obj):
        return obj.employee.get_department_display()


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
