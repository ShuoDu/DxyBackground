# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def decode(info):
      return info.decode('utf-8')


# 店铺类型表
class messageType(models.Model):
    class Meta:
        verbose_name = '消息类型'
        verbose_name_plural = '消息类型'
    name = models.CharField(max_length=20, verbose_name='消息类型')  # 消息类型

    def __str__(self):
        return "%s" % self.name

    def toDict(self):
        return {'name': self.name}


#  首页消息列表
class main_message(models.Model):
    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
    message_type = models.ForeignKey('messageType')
    id = models.AutoField(primary_key=True)  # 自增主键
    title = models.CharField(max_length=200, verbose_name='新闻标题')  # 新闻标题
    content = models.CharField(max_length=5000, verbose_name='新闻内容')  # 新闻内容
    address = models.CharField(max_length=200, verbose_name='出处')  # 新闻出处
    time = models.CharField(max_length=200, verbose_name='新闻发布时间')  # 新闻发布时间
    message_img = models.ImageField(upload_to='img', verbose_name='消息图片')  # 消息图片
    list_filter = ['title']
    search_fields = ['title']

    # 变更成json类型
    def toDict(self):
        return {'title': self.title, 'content': self.content, 'address': self.address, 'time': self.time,
                'message_img': "http://127.0.0.1:8080" + self.message_img.url}

    def __str__(self):
        return "%s" % self.title


# 服务类型
class service_type(models.Model):
    class Meta:
        verbose_name = '服务类型'
        verbose_name_plural = '服务类型'
    service_name = models.CharField(max_length=200, verbose_name='服务名称')

    def __str__(self):
        return "%s" % self.service_name

    def toDict(self):
        return {'name': self.service_name}


# 服务细分类型
class service_detail_type(models.Model):
    class Meta:
        verbose_name = '服务类型具体分类'
        verbose_name_plural = '服务类型具体分类'
    service_type = models.ForeignKey('service_type')
    service_name = models.CharField(max_length=200, verbose_name='具体类别')

    def __str__(self):
        return "%s" % self.service_name

    def toDict(self):
        return {'name': self.service_name}


# 服务信息
class service_message(models.Model):
    class Meta:
        verbose_name = '服务信息'
        verbose_name_plural = '服务信息'
    id = models.AutoField(primary_key=True)  # 自增主键
    service_type = models.ForeignKey('service_detail_type')
    title = models.CharField(max_length=200, verbose_name='消息标题')  # 新闻标题
    content = models.CharField(max_length=5000, verbose_name='消息内容')  # 新闻内容
    address = models.CharField(max_length=200, verbose_name='出处')  # 新闻出处
    time = models.CharField(max_length=200, verbose_name='发布时间')  # 新闻发布时间

    def __str__(self):
        return "%s" % self.title

    def toDict(self):
        return {'title': self.title, 'content': self.content, 'address': self.address}


# 消息图片
class message_img(models.Model):
    class Meta:
        verbose_name = '消息图片'
        verbose_name_plural = '消息图片'
    measage_key = models.ForeignKey('service_message')
    message_img = models.ImageField(upload_to='img', verbose_name='消息图片')  # 消息图片

    def __str__(self):
        return "%s" % self.message_img

    def toDict(self):
        return {'img_url': self.message_img}
