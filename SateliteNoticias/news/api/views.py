from rest_framework import generics, status,viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from news.api.permissions import IsAuthorOrReadOnly
from news.api.serializers import EditionSerializer, Newserializer
from news.models import Edition, News


import logging

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = Newserializer
    #Only authors can delete their News
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NewsListAPIView(generics.ListAPIView):
    serializer_class = Newserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        listFormat = self.kwargs.get('value')
        #Convertirlo a lista
        listFormat = listFormat.split("-")
        #Primer filtro
        
        firstFilter = News.objects.filter(tags__name__in=[listFormat[0]]).distinct()
        #Sacarle el primer elemento 
        listFormat.pop(0)
        tags = listFormat
        results = firstFilter
        #Iterar para realizar filtros con los que quedan
        for tag in tags:
            results = results.filter(tags__name__in=[tag])


        return results.order_by("-created_at")
        
class EditionCreateAPIView(generics.CreateAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        news = get_object_or_404(News, slug=kwarg_slug)

        if news.editions.filter(author=request_user).exists():
            raise ValidationError("You have already editioned this news!")

        serializer.save(author=request_user, news=news)


class EditionListAPIView(generics.ListCreateAPIView):
    serializer_class = EditionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        logging.debug('aqui va algo')
        logging.debug(type(Edition.objects.filter(news__slug=kwarg_slug).order_by("-created_at")))
        logging.debug(Edition.objects.filter(news__slug=kwarg_slug).order_by("-created_at"))
        return Edition.objects.filter(news__slug=kwarg_slug).order_by("-created_at")


class EditionRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]



class EditionLikeAPIView(APIView):
    serializer_class = EditionSerializer
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        edition = get_object_or_404(Edition, pk=pk)
        user = request.user

        edition.voters.remove(user)
        edition.save()

        serializer_context= {"request":request}
        serializer = self.serializer_class(edition, context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        edition = get_object_or_404(Edition, pk=pk)
        user = request.user

        edition.voters.add(user)
        edition.save()

        serializer_context= {"request":request}
        serializer = self.serializer_class(edition, context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)