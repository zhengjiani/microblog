import os
<<<<<<< HEAD
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:zhengjiani88@localhost:3306/microblog'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['936089353@qq.com']
    POSTS_PER_PAGE = 25
=======
class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://*:*@localhost:3306/microblog'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> cb42cf1161480375b2e587f432535d5c4f2c0e80
