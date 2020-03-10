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
        serializer.save(author=self.request.user)

class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        listFormat = self.kwargs.get('value')
        #Convertirlo a lista
        listFormat = listFormat.split("-")
        #Primer filtro
        
        firstFilter = Question.objects.filter(tags__name__in=[listFormat[0]]).distinct()
        #Sacarle el primer elemento 
        listFormat.pop(0)
        tags = listFormat
        results = firstFilter
        #Iterar para realizar filtros con los que quedan
        for tag in tags:
            results = results.filter(tags__name__in=[tag])


        return results.order_by("-created_at")
        
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