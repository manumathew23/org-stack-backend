from rest_framework import serializers


class QuestionsSerializer(serializers.Serializer):
    name = serializers.CharField()
    tagline = serializers.CharField(max_length=200)
    description = serializers.CharField()
