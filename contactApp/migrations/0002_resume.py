# Generated by Django 3.2.7 on 2021-09-20 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('personID', models.CharField(max_length=30, verbose_name='身份证号')),
                ('sex', models.CharField(default='男', max_length=5, verbose_name='性别')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('birth', models.DateField(default='2021-09-20', max_length=20, verbose_name='出生日期')),
                ('edu', models.CharField(default='本科', max_length=5, verbose_name='学历')),
                ('school', models.CharField(max_length=40, verbose_name='毕业院校')),
                ('major', models.CharField(max_length=40, verbose_name='专业')),
                ('position', models.CharField(max_length=40, verbose_name='申请职位')),
                ('experience', models.TextField(blank=True, null=True, verbose_name='学习或工作经历')),
                ('photo', models.ImageField(upload_to='contact/recruit/%Y_%m_%d', verbose_name='个人照片')),
                ('status', models.IntegerField(choices=[(1, '未审'), (2, '通过'), (3, '未通过')], default=1, verbose_name='面试成绩')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='提交时间')),
            ],
            options={
                'verbose_name': '简历',
                'verbose_name_plural': '简历',
                'ordering': ('-status', '-publishDate'),
            },
        ),
    ]
