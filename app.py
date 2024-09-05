from flask import Flask, render_template
from exts import db, mail
from blueprints.auth import auth_bp
from blueprints.qa import qa_bp
import config
from models import UserModel
from flask_migrate import Migrate

app = Flask(__name__)

# bind config file
app.config.from_object(config)
# bind db
db.init_app(app)
# bind mail
mail.init_app(app)
# bind migrate
migrate = Migrate(app, db)


# register blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)


@app.route('/')
def index():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
