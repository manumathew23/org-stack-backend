from rest_framework.views import APIView
from .models import Questions


class QuestionsView(APIView):
    def get(self):
        questions = Questions.objects.all()
        return questions
