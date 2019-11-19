from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Questions
from .serializers import QuestionsSerializer


class QuestionsView(APIView):
    def get(self, request, pk=None):
        breakpoint()
        if pk is not None:
            questions = Questions.objects.filter(pk=pk).values()
        else:
            questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        # import pdb
        # pdb.set_trace() #debug point
        # breakpoint()
        serializer = QuestionsSerializer(data=data)
        if serializer.is_valid():
            questions = Questions(**data)
            questions.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response(0)

    def patch(self, request):
        return Response(0)

    def delete(self, request):
        return Response(0)
