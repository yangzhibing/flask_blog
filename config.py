import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 设置密码，最好是别人才不到的随机码
    SECRET_KEY = '1a2s3d4f5g$%R%jgpoiu'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False