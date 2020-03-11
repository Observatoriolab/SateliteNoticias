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

    path("news/<slug:slug>/answers/",
        qv.AnswerListAPIView.as_view(),
        name="answer-list"),

    path("news/<slug:slug>/answer/",
        qv.AnswerCreateAPIView.as_view(),
        name="answer-create"),

     path("answers/<int:pk>/",
        qv.AnswerRUDAPIView.as_view(),
        name="answer-detail"),

     path("answers/<int:pk>/like/",
        qv.AnswerLikeAPIView.as_view(),
        name="answer-like")
]
    

