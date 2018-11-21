# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import os
import pymysql
DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/bbs?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

CMS_USER_ID = 'DSADSAD1551512'

# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = '1125365907@qq.com'
MAIL_PASSWORD = 'fymamdgjrovehgcd'
MAIL_DEFAULT_SENDER = '1125365907@qq.com'

#阿里大于短信配置
ALIDAYU_APP_KEY = 'LTAIGEGh0PMlgqX3'
ALIDAYU_APP_SECRET = 'eWiD8gVU2W0Qx5eBc5JU45qbHoO0bi'
ALIDAYU_SIGN_NAME = "知了课堂论坛"
ALIDAYU_TEMPLATE_CODE = 'SMS_149385941'
