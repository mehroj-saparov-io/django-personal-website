from django.urls import path
from .views import (
    home_view,
    blog_view,
    blog_detail_view,
    about_view,
    lectures_view,
    projects_view,
    contact_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("blog/", blog_view, name="blog"),
    path("blog/<slug:slug>/", blog_detail_view, name="blog_detail"),
    path("about/", about_view, name="about"),
    path("lectures/", lectures_view, name="lectures"),
    path("projects/", projects_view, name="projects"),
    path("contact/", contact_view, name="contact"),
]
