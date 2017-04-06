from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from ProjectTracking.models import Requirement, Employee


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['r_info_name',
    #           'r_info_submit_time',
    #           # 'r_info_submit_department',
    #           # 'r_info_submit_person',
    #           'r_info_submit_employee',
    #           'r_info_value',
    #           # 'r_category',
    #           # 'r_leader',
    #           ]
    list_display = ('r_info_name',
                    'r_info_submit_time',
                    # 'r_info_submit_employee',
                    # 'r_info_submit_department',
                    # 'r_info_submit_person',
                    # 'r_info_value',
                    # 'r_category',
                    # 'r_leader',
                    )


admin.site.register(Requirement, QuestionAdmin)


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
        for k, v in Employee.DEPARTMENT_CHOICES:
            if k == obj.employee.department:
                return v
        return '-'


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
