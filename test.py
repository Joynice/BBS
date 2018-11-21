# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import top.api

app_key = 'LTAIGEGh0PMlgqX3'
app_secret = 'eWiD8gVU2W0Qx5eBc5JU45qbHoO0bi'
req = top.setDefaultAppInfo(app_key,app_secret)
req = top.api.AlibabaAliqinFcSmsNumSendRequest()
req.extend = ""
req.sms_type = 'normal'
req.sms_free_sign_name = '知了课堂论坛'
# 给模版的参数
telphone_captcha = 123456
telphone = 15225090724
req.sms_param = "{code:'%s'}" % telphone_captcha
req.rec_num = telphone
req.sms_template_code = 'SMS_149385941'

resp = req.getResponse()
print(resp)



