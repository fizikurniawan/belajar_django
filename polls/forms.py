from django.forms import ModelForm, Textarea
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
