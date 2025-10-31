
from django.urls import path

from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("draft-list/", views.DraftListView.as_view(), name="draft-list"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view(), name="draft-detail"),
    path("post-create/", views.PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("draft-publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft-publish"),
    path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)