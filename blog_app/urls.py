
from django.urls import path

from blog_app import views

urlpatterns = [
    path("", view.post_list, name="post-list"),
]
