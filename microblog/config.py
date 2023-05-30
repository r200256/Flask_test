import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('smtp.spaceweb.ru')    
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS= os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('555')
    MAIL_PASSWORD = os.environ.get('16112017NoteBook')
    admins = ['555@aromika.info']
