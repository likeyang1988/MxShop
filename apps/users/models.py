#pep8的规范，系统包最前面，第三方包次之，自己导入的文件最后

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息,在seting中 添加配置AUTH_USER_MODEL = 'users.UserProfile' 才能替换系统用户
    null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空，即在Null字段显示为YES。
blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    #用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField(max_length=30, null=True, blank=True,verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True,verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female",verbose_name="性别")
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code