from rest_framework import generics, status,viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


import logging

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = QuestionSerializer
    #Only authors can delete their question
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        #self.request.data.tags (aqui deberia estar el tema)
        #Si es que existe el filtro
        if('filter' in self.request.data):
            logging.debug('este es el filtro que voy a aplicar')
            lista = self.request.data.get("tags","")
            '''
            logging.debug(type(lista))
            logging.debug(lista[0])
            logging.debug(lista)
            '''
            firstFilter = Question.objects.filter(tags__name__in=[lista[0]]).distinct()
            lista.pop(0)
            tags = lista
            results = firstFilter
            for tag in tags:
                results = results.filter(tags__name__in=[tag])

            logging.debug('ojala')

            '''
            logging.debug('asi quedo el auxiliar')
            logging.debug(auxiliar)
            logging.debug(filteredQuestions)
            '''
            return results
        else:
            serializer.save(author=self.request.user)


    def get_queryset(self):
        
        return  Question.objects.all().order_by("-created_at")

class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        firstFilter = Question.objects.filter(tags__name__in=[self.kwargs.get('value')]).distinct()
        return firstFilter.order_by("-created_at")
        
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question!")

        serializer.save(author=request_user, question=question)


class AnswerListAPIView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        logging.debug('aqui va algo')
        logging.debug(type(Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")))
        logging.debug(Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at"))
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]



class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context= {"request":request}
        serializer = self.serializer_class(answer, context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.add(user)
        answer.save()

        serializer_context= {"request":request}
        serializer = self.serializer_class(answer, context = serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)