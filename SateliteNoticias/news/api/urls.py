from django.urls import include, path
from rest_framework.routers import DefaultRouter
from news.api import views as qv

router = DefaultRouter()
router.register(r"news", qv.NewsViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("news/tags/<str:value>/",
        qv.NewsListAPIView.as_view(),
        name="news-list"),

    path("news/<slug:slug>/editions/",
        qv.EditionListAPIView.as_view(),
        name="edition-list"),

    path("news/<slug:slug>/edition/",
        qv.EditionCreateAPIView.as_view(),
        name="edition-create"),

     path("editions/<int:pk>/",
        qv.EditionRUDAPIView.as_view(),
        name="edition-detail"),

     path("editions/<int:pk>/like/",
        qv.EditionLikeAPIView.as_view(),
        name="edition-like")
]
    

