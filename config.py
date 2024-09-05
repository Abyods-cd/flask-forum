# config.py

# database configuration
HOSTNAME = '127.0.0.1'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'zy123456'
DATABASE = 'FlaskForum'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOSTNAME + ':' + PORT + '/' + DATABASE

# email configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "avod.zy@gmail.com"
# MAIL_PASSWORD = "123"
MAIL_DEFAULT_SENDER = "avod.zy@gmail.com"