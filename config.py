# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import os
import pymysql
import redis

DEBUG = True
# SECRET_KEY = os.urandom(24)
SECRET_KEY = 'dsadas1231d3sa'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/bbs?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

CMS_USER_ID = 'DSADSAD1551512'
FRONT_USER_ID = 'DHDIUASHDIUSAUHDUIASHDUIASHDUI1541646DSADAS'

# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = '1125365907@qq.com'
MAIL_PASSWORD = 'fymamdgjrovehgcd'
MAIL_DEFAULT_SENDER = '1125365907@qq.com'

# 阿里大于短信配置
ALIDAYU_APP_KEY = 'LTAIGEGh0PMlgqX3'
ALIDAYU_APP_SECRET = 'eWiD8gVU2W0Qx5eBc5JU45qbHoO0bi'
ALIDAYU_SIGN_NAME = "知了课堂论坛"
ALIDAYU_TEMPLATE_CODE = 'SMS_149385941'

#配置ueditor上传七牛云配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "Yd6OKMlBkKIeC2RDMFYQnNXVOwCrOTkL0Vd0uV6Q"
UEDITOR_QINIU_SECRET_KEY = "rdAaGakOIt3bOwic-AkIzuHFboJiXCKLUolGJ8mP"
UEDITOR_QINIU_BUCKET_NAME = "joynice"
UEDITOR_QINIU_DOMAIN = "http://piy7lmw45.bkt.clouddn.com"

#flask前端帖子分页配置
EVERY_COUNT = 10

#flask后端帖子分页配置
BACK_COUNT = 12

#celery相关的配置
CELERY_RESULT_BACKEND = 'redis://192.168.0.119:6379/14'
CELERY_BROKER_URL = 'redis://192.168.0.119:6379/14'

