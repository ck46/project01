from rest_framework import serializers
from digestai.models import StudySet, User


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'fullname',
            'email',
        )
