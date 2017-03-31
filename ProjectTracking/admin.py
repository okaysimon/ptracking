from django.contrib import admin
from ProjectTracking.models import Requirement


class QuestionAdmin(admin.ModelAdmin):
    fields = ['r_info_name',
              'r_info_submit_time',
              'r_info_submit_department',
              'r_info_submit_person',
              'r_info_value',
              # 'r_category',
              # 'r_leader',
              ]
    list_display = ('r_info_name',
                    'r_info_submit_time',
                    'r_info_submit_department',
                    'r_info_submit_person',
                    # 'r_info_value',
                    # 'r_category',
                    # 'r_leader',
                    )

admin.site.register(Requirement, QuestionAdmin)
