from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic.edit import CreateView

from .models import Subject, Topic, Flashcard

from .forms import NewSubjectForm, NewTopicForm

from django.urls import reverse_lazy

# Create your views here.
def StudyView(request):
    return render(request, "study.html")

# Pomodoro Technique View
class PomodoroTimerView(TemplateView):
    template_name = "pomodoro_timer.html"

# Flashcards Technique View
def subjectView(request):
    subjects = SubjectListView.as_view()(request)
    topics  = TopicListView.as_view()(request)

    context = {}
    context.update(subjects.context_data)
    context.update(topics.context_data)

    return render(request, "subjects.html", context=context)

class SubjectCreateView(CreateView):
    model = Subject
    fields = ["name"]
    success_url = reverse_lazy("topic_add")
    template_name = "subject_add.html"

class SubjectListView(ListView):
    model = Subject

class TopicCreateView(CreateView):
    model = Topic
    fields = ["subject", "name"]
    template_name = "topic_add.html"
    success_url = reverse_lazy("flashcard_add")

class TopicListView(ListView):
    model = Topic
    fields = ["name"]

class TopicDetailView(DetailView):
    template_name = "topic_detail.html"
    model = Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flashcards"] = Flashcard.objects.all()
        return context

class FlashcardCreateView(CreateView):
    model = Flashcard
    fields = ["topic", "question", "answer"]
    template_name = "flashcard_add.html"
    success_url = reverse_lazy("subjects")

class FlashcardListView(ListView):
    model = Flashcard
    fields = ["question", "answer"]



















# Future References
def SubjectView(request):
    newSubject = SubjectCreateView.as_view()(request)
    newTopic = TopicCreateView.as_view()(request)
    subjects = SubjectListView.as_view()(request)
    topics = TopicListView.as_view()(request)

    context = {}
    context.update(newSubject.context_data)
    context.update(subjects.context_data)
    context.update(topics.context_data)
    #context.update(newTopic.context_data)

    return render(request, "subjects.html", context=context)


def SubjectView(request):
    if request.method == "POST":
        print(request.POST)
        subjForm = NewSubjectForm(request.POST)
        topicForm = Topic.objects.create(request.POST)
        if subjForm.is_valid():
            subjForm.save()
            print("Subject saved!")
            return redirect("subjects")
        
        elif topicForm.is_valid():
            topicForm.save()
            print("topic saved!")
            return redirect("subjects")
        else:
            print("No valid forms available!")
    
    context = {
        "subjects": Subject.objects.all(), # SubjectListView
        "topics": Topic.objects.all(), # TopicListView
        "NewSubject": NewSubjectForm,
        "NewTopic": Subject,
    }
    return render(request, "subjects.html", context=context)