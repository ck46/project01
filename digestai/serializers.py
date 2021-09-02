from rest_framework import serializers
from digestai.models import StudySet


class StudySetSerializer(serializers.ModelSerializer):
    flashcards = serializers.ListField()
    quiz = serializers.ListField()

    class Meta:
        model = StudySet
        fields = (
            'id',
            'username',
            'author',
            'title',
            'summary',
            'quiz',
            'flashcards',
        )

