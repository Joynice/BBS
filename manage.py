# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import create_app
from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission
FrontUser = front_models.FrontUser
app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功!')
        else:
            print('没有这个角色：{}'.format(role))
    else:
        print('{}：这个邮箱没有被注册'.format(email))


@manager.command
def create_role():
    # 1. 访问者（可以修改个人信息）
    visitor = CMSRole(name='访问者', desc='只能访问数据，不能修改。')
    visitor.permissions = CMSPermission.VISITOR
    # 2.运营人员（修改个人信息，管理帖子，管理评论，管理前台用户）
    operator = CMSRole(name='运营人员', desc='修改个人信息，管理帖子，管理评论，管理前台用户。')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.COMMENTER | CMSPermission.PRONTUSER
    # 3.管理员（拥有绝大多数权限）
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限。')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.COMMENTER | \
                        CMSPermission.CMSUSER | CMSPermission.PRONTUSER | CMSPermission.BOARDER

    # 4.开发者
    developer = CMSRole(name='开发者', desc='开发者专用角色。')
    developer.permissions = CMSPermission.ALL_PERMISSON

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.command
def test_permission():
    user = CMSUser.query.first()
    if user.has_permission(CMSPermission.VISITOR):
        print('这个角色有访问者权限！')
    else:
        print('这个角色没有访问者权限！')
@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u','--username', dest='username')
@manager.option('-p','--password',dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
