import os 
basedir=os.path.abspath(os.path.dirname(__file__)) #skapar i praktiken en fil för en databas (app.db) 

class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') #Berättar vad hemsidan ska göra om det inte finns någon variabel definierad i den kallade databasen. 
    SQLALCHEMY_TRACK_MODIFICATIONS=False #Stänger av en del av SQLAlchemy som inte ska användas. 

    MAIL_SERVER= os.environ.get('MAIL_SERVER')
    MAIL_PORT= int(os.environ.get('MAIL_PORT') or 25) 
    MAIL_USE_TLS= os.environ.get('MAIL_USE_TLS') is not None 
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
    ADMINS= ['insert_email']
    POSTS_PER_PAGE= 25
    LANGUAGES=['en']
