# Generated by Django 3.0 on 2021-07-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deepureuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('mpno', models.CharField(max_length=11, verbose_name='手机号')),
                ('openid', models.CharField(max_length=64, verbose_name='openid')),
                ('sex', models.IntegerField(verbose_name='性别:0:女 1:男')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='bim')),
                ('bodyfatratio', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='体脂率')),
                ('other', models.CharField(max_length=20, null=True, verbose_name='锻炼习惯 1:跑步 2：健身房 3：自己在家 4：很少锻炼 5：其他形式')),
            ],
            options={
                'verbose_name': '渠道分类表',
                'verbose_name_plural': '渠道分类表',
                'db_table': 'crawler_categroy',
            },
        ),
    ]
