from django import forms
from django.forms import inlineformset_factory
from .models import Exam, Question, Choice


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del examen'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descripción detallada del examen'}),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['statement', 'score']
        widgets = {
            'statement': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enunciado de la pregunta'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
        labels = {
            'statement': 'Enunciado de la Pregunta',
            'score': 'Puntaje',
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Texto de la opción'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'text': 'Opción',
            'is_correct': '¿Es Correcta?',
        }


ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    fields=['text', 'is_correct'],
    extra=4,
    min_num=2,
    validate_min=True,
    can_delete=True
)
