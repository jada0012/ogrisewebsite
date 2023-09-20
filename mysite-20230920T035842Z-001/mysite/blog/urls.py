from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UnauthenticatedPostView, ResourcesView, ResourceDetailView, home, showRecentArticles, test, EngageView, EngageDetailView

urlpatterns = [
    path("articles", HomeView.as_view(), name="article-list"),
    path("articles/add_post", AddPostView.as_view(), name="add-post"),

    path("resources", ResourcesView.as_view(), name="resource-list"),
    path("involvement", EngageView.as_view(), name="involvement-list"),
    path("articles/<slug:slug>", ArticleDetailView.as_view(), name="article-detail"),
    path("resources/<slug:slug>", ResourceDetailView.as_view(), name="resource-detail"),
    path("involvement/<slug:slug>", EngageDetailView.as_view(), name="involvement-detail"),
    path("articles/queue", UnauthenticatedPostView.as_view(), name="article-queue"),
    path("", home, name="home-page"),
    path("articles/show_recent", showRecentArticles, name="recent-articles"),
    path("test/", test, name='test'),
]