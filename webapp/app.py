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
    # app, "kubeflow-news.com", [3408], "kubeflow-news", "/", [3184, 3265]
    app, "kubeflow-news.com", [2510], "ai", "/", [3184, 3265]
)


@app.template_filter('pluralize')
def pluralize_filter(total_posts):
    if int(total_posts) > 1:
        return "s"
    else:
        return ""
