from rest_framework import serializers
from .models import Question,Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "title",
            "code_file",
            "description",
            "user",
            "ask_date",
            "is_active",
            "is_pin",
            "is_verify",
            "is_solve",
            )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "user",
            "description",
            "is_active",
            "is_best",
            "write_date",
            "question",
            )
