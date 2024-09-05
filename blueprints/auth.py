import string
import redis
from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message
from flask import request
import random

# create auth blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# config redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/register')
def register():
    return render_template('register.html')

@auth_bp.route('/captcha/email')
def getEamilCaptcha():
    email = request.args.get('email')
    source = string.digits * 4
    captcha = "".join(random.sample(source, 4))
    # save captcha to redis and set expire time to 100s
    redis_client.setex(f'captcha:{email}', 100, captcha)
    message = Message(subject='Hello, Mail Test', recipients=[email], body=captcha)
    mail.send(message)
    return 'Send Mail Success'

@auth_bp.route('/captcha/verify')
def verifyCaptcha():
    email = request.args.get('email')
    userCaptcha = request.args.get('captcha')
    storedCaptcha = redis_client.get(f'captcha:{email}')
    if userCaptcha == storedCaptcha:
        return 'Captcha Verify Success'
    else:
        return 'Captcha Verify Failed'
# # send mail
# @auth_bp.route('/test')
# def test():
#     message = Message(subject='Hello, Mail Test', recipients=['yuanz@u.nus.edu'], body='Hello, This is a test mail')
#     mail.send(message)
#     return 'Send Mail Success'