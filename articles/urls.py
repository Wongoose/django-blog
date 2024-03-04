from django.urls import path
from django.urls import re_path
from . import views

app_name = "articles"

# URL conf
urlpatterns = [
    re_path(r"^$", views.articleList, name="list"),
    re_path(r"^create/$", views.articleCreate, name="create"),
    re_path(r"^(?P<slug>[\w-]+)/$", views.articleDetails, name="details"), # name it <slug> and regex restrictions (allow -), "$"" means at the end
]