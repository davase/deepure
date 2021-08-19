from django.db import models
from django.apps import apps
#用户注册表
class Deepureuser(models.Model):
    name = models.CharField(max_length=64,verbose_name="姓名")
    mpno = models.CharField(max_length=11,verbose_name="手机号")
    openid = models.CharField(max_length=64,verbose_name="openid")
    sex = models.IntegerField(verbose_name="性别:0:女 1:男")
    age = models.IntegerField(verbose_name="年龄")
    bmi = models.CharField(max_length=15,verbose_name="bmi")
    bodyfatratio = models.CharField(max_length=15,verbose_name="体脂率")
    other = models.CharField(max_length=20,null=True,verbose_name="锻炼习惯 1:跑步 2：健身房 3：自己在家 4：很少锻炼 5：其他形式")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = '用户注册表'
        db_table = 'deepure_user'