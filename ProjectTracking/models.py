from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Employee(models.Model):
    DEPARTMENT_ZONGCAISHI = 0
    DEPARTMENT_ZONGHE = 1
    DEPARTMENT_CAIWU = 2
    DEPARTMENT_CHUANGXIN = 3
    DEPARTMENT_WANGXIAO = 4
    DEPARTMENT_CHANXIAN = 5
    DEPARTMENT_SHOUXIAN = 6
    DEPARTMENT_SHUJU = 7
    DEPARTMENT_XINXI = 8
    DEPARTMENT_CHOICES = (
        (DEPARTMENT_ZONGCAISHI, '总裁室'),
        (DEPARTMENT_ZONGHE, '综合部'),
        (DEPARTMENT_CAIWU, '财务部'),
        (DEPARTMENT_CHUANGXIN, '创新业务部'),
        (DEPARTMENT_WANGXIAO, '网络销售部'),
        (DEPARTMENT_CHANXIAN, '产险销售部'),
        (DEPARTMENT_SHOUXIAN, '寿险电销部'),
        (DEPARTMENT_SHUJU, '数据管理部'),
        (DEPARTMENT_XINXI, '信息技术部'),
    )

    user = models.OneToOneField(User)
    person = models.CharField('姓名', max_length=10)
    department = models.IntegerField('部门', choices=DEPARTMENT_CHOICES, default=DEPARTMENT_ZONGCAISHI)


def validate_file_extension(value):
    if hasattr(value.file, 'content_type'):
        if value.file.content_type not in ['application/msword',
                                           'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
            raise ValidationError(u'File not supported!')
    else:
        if not value.file.name.endswith('.docx') and not value.file.name.endswith('.doc'):
            raise ValidationError(u'File not supported!')


class Requirement(models.Model):
    CATEGORY_DEVELOPMENT = '0'
    CATEGORY_OPERATION = '1'
    CATEGORY_EMERGENCY = '2'
    REQUIREMENT_CATEGORY = (
        (CATEGORY_DEVELOPMENT, '开发类'),
        (CATEGORY_OPERATION, '运维类'),
        (CATEGORY_EMERGENCY, '紧急类'),
    )

    r_id = models.AutoField('ID', primary_key=True)
    i_name = models.CharField('需求名称', max_length=100, unique=True)
    i_submit_time = models.DateTimeField('提交时间')
    i_submit_user = models.ForeignKey(User, verbose_name='提出用户', default=0)
    i_value = models.CharField('价值', max_length=500, default='无')
    i_file = models.FileField('需求文档', upload_to='uploads/', validators=[validate_file_extension])
    # r_file_framework = models.FileField('架构文档', upload_to='uploads/')

    r_category = models.CharField('需求类别', max_length=1, choices=REQUIREMENT_CATEGORY, default='', blank=True, null=True)
    # r_leader = models.CharField('任务负责人', max_length=20, default=None, blank=True, null=True)
    # r_value_ok = models.BooleanField(default=False, blank=True)
    # r_handle = models.CharField('需求流转地', max_length=50, default=None, blank=True, null=True)
    # r_status = models.CharField('需求流程状态', max_length=50, default=None, blank=True, null=True)
    # r_workload = models.FloatField('工作量', default=None, blank=True, null=True)
