from  djongo import models

class User(models.Model):
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

class Answer(models.Model):
    option = models.CharField(max_length=1)
    detail = models.CharField(max_length=255)

    class Meta:
        abstract = True

class MultipleChoiceQuestion(models.Model):
    question = models.CharField(max_length=255)
    options = models.ArrayField(model_container=Answer, default=None)
    answer = models.CharField(max_length=1)

    class Meta:
        abstract = True


class FlashCard(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=255)
    studied = models.BooleanField(default=False)

    class Meta:
        abstract = True

class StudySet(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=2000, default='')
    quiz = models.ArrayField(model_container=MultipleChoiceQuestion, default=None)
    flashcards = models.ArrayField(model_container=FlashCard, default=None)

