from canonicalwebteam.blog.app import BlogExtension
from canonicalwebteam.flask_base.app import FlaskBase
import datetime


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
    app,
    "kubeflow-news.com",
    [1239],
    "design",
    "/",
    [3184, 3265],
)


@app.template_filter("pluralize")
def pluralize_filter(total_posts):
    if int(total_posts) > 1:
        return "s"
    else:
        return ""


@app.template_filter("descending_years")
def descending_years_filter(end_year):
    now = datetime.datetime.now()
    return range(now.year, end_year, -1)


@app.template_filter("months_list")
def months_list_filter(year):
    months = []
    now = datetime.datetime.now()
    for i in range(1, 13):
        date = datetime.date(year, i, 1)
        if date < now.date():
            months.append({"name": date.strftime("%b"), "number": i})
    return months
