import flask
from canonicalwebteam.blog.app import BlogExtension
from canonicalwebteam.flask_base.app import FlaskBase


app = FlaskBase(
    __name__,
    "kubeflow-news.com",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)


blog = BlogExtension(
    app, "kubeflow-news.com", [3408], "kubeflow-news", "/", [3184, 3265]
)


@app.errorhandler(404)
def not_found_error(error):
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return flask.render_template("500.html"), 500
