from flask import Flask
from .extensions import db, login_manager
from .auth.routes import auth_bp
from .salary.routes import salary_bp
from .finance.routes import finance_bp
from .dashboard.routes import dashboard_bp
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(salary_bp)
    app.register_blueprint(finance_bp)
    app.register_blueprint(dashboard_bp)

    return app