from flask import Blueprint, render_template

# Blueprint를 사용해서 auth를 생성한다
auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# index 엔드포인트를 작성한다
@auth.route("/")
def index():
    return render_template("auth/index.html")