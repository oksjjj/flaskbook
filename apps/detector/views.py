from flask import Blueprint, render_template

# template_folder를 지정한다 (static은 지정하지 않는다)
dt = Blueprint("detector", __name__, template_folder="templates")

# dt 애플리케이션을 사용하여 엔드포인트를 작성한다
@dt.route("/")
def index():
    return render_template("detector/index.html")