from django.forms import ModelForm, Textarea
from .models import Question, Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
