# -*- coding: UTF-8 -*-、
"""
celery 启动命令:celery -A tasks.celery worker --pool=eventlet， 启动时保证与tasks.py同级
若出现 'AttributeError: 'float' object has no attribute 'items'错误，这是redis包版本不兼容，退回2.10.6版本即可。
pip install redis==2.10.6
"""




