from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config

# SQLAlchemy를 인스턴스화한다
db = SQLAlchemy()

csrf = CSRFProtect()

# LoginManager를 인스턴스화한다
login_manager = LoginManager()

# login_view 속성에 미 로그인 시 리다이렉ㅌ하는 엔드포인트를 지정한다
login_manager.login_view = "auth.signup"

# login_manager 속성에 로그인 후에 표시할 메시지를 지정한다
# 여기에서는 아무 것도 표시하지 않도록 공백을 지정한다

login_manager.login_message = ""

# config의 키를 전달한다
def create_app(config_key):
    # 플라스크 인스턴스 생성
    app = Flask(__name__)

    # config_key에 매치되는 환경의 config 클래스를 읽어 들인다
    app.config.from_object(config[config_key])

    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)

    csrf.init_app(app)

    # Migrate와 앱을 연계한다
    Migrate(app, db)

    # login_manager를 애플리케이션과 연계한다
    login_manager.init_app(app)

    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views

    # register_blueprint를 사용해 views의 crud를 앱에 등록한다
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # 이제부터 작성하는 auth 패키지로부터 views를 import한다
    from apps.auth import views as auth_views

    # register_blueprint를 사용해 views의 auth를 앱에 등록한다
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app