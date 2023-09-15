from django.urls import path

from .views import StudyView, subjectView, PomodoroTimerView
from.views import FlashcardCreateView, TopicCreateView, SubjectCreateView, TopicDetailView

urlpatterns = [
    path("", StudyView, name="study"),
    path("pomodoro_timer/", PomodoroTimerView.as_view(), name="pomodoro_timer"),
    path("subjects/", subjectView, name="subjects"),
    path("subjects/flashcard_add/", FlashcardCreateView.as_view(), name="flashcard_add"),
    path("topic_add/", TopicCreateView.as_view(), name="topic_add"),
    path("subject_add/", SubjectCreateView.as_view(), name="subject_add"),
    path("subjects/topic_detail/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
]
