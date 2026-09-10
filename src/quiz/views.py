from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet


def exam_list(view_request):
    exams = Exam.objects.all()
    return render(view_request, 'quiz/exam_list.html', {'exams': exams})


def exam_detail(view_request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.choices.all() # related_name='choices' on Question.exam points to questions
    return render(view_request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})


def question_create(view_request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    
    if view_request.method == 'POST':
        question_form = QuestionForm(view_request.POST)
        formset = ChoiceFormSet(view_request.POST)
        
        if question_form.is_valid() and formset.is_valid():
            # Validate that exactly one choice is marked as correct
            correct_count = 0
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    if form.cleaned_data.get('is_correct', False):
                        correct_count += 1
            
            if correct_count != 1:
                messages.error(view_request, 'Debe haber exactamente una opción marcada como correcta.')
            else:
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()
                
                formset.instance = question
                formset.save()
                
                messages.success(view_request, 'Pregunta y opciones guardadas exitosamente.')
                return redirect('quiz:exam_detail', exam_id=exam.pk)
        else:
            messages.error(view_request, 'Por favor, corrija los errores en el formulario.')
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()
        
    return render(view_request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset
    })


def exam_create(view_request):
    if view_request.method == 'POST':
        form = ExamForm(view_request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(view_request, 'Examen creado exitosamente.')
            return redirect('quiz:exam_detail', exam_id=exam.pk)
    else:
        form = ExamForm()
    return render(view_request, 'quiz/exam_form.html', {'form': form})
