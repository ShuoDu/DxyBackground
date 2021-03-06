# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main_message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('content', models.CharField(max_length=5000, verbose_name='\u65b0\u95fb\u5185\u5bb9')),
                ('address', models.CharField(max_length=200, verbose_name='\u51fa\u5904')),
                ('time', models.CharField(max_length=200, verbose_name='\u65b0\u95fb\u53d1\u5e03\u65f6\u95f4')),
                ('message_img', models.ImageField(upload_to='img', verbose_name='\u6d88\u606f\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u65b0\u95fb',
                'verbose_name_plural': '\u65b0\u95fb',
            },
        ),
        migrations.CreateModel(
            name='message_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_img', models.ImageField(upload_to='img', verbose_name='\u6d88\u606f\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u6d88\u606f\u56fe\u7247',
                'verbose_name_plural': '\u6d88\u606f\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='messageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6d88\u606f\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u6d88\u606f\u7c7b\u578b',
                'verbose_name_plural': '\u6d88\u606f\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='service_detail_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, verbose_name='\u5177\u4f53\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u7c7b\u578b\u5177\u4f53\u5206\u7c7b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b\u5177\u4f53\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='service_message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='\u6d88\u606f\u6807\u9898')),
                ('content', models.CharField(max_length=5000, verbose_name='\u6d88\u606f\u5185\u5bb9')),
                ('address', models.CharField(max_length=200, verbose_name='\u51fa\u5904')),
                ('time', models.CharField(max_length=200, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMessage.service_detail_type')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='service_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, verbose_name='\u670d\u52a1\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='service_detail_type',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMessage.service_type'),
        ),
        migrations.AddField(
            model_name='message_img',
            name='measage_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMessage.service_message'),
        ),
        migrations.AddField(
            model_name='main_message',
            name='message_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainMessage.messageType'),
        ),
    ]
