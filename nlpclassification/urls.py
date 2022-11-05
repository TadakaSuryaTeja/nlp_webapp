from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question-answering/", views.question_answering, name="question-answering"),
    path("masked-word/", views.masked_word, name='masked-word'),
    path("summarization/", views.summarization, name='summarization'),
    path("sentiment-analysis/", views.sentiment_analysis_view, name='sentiment-analysis'),
    path("text-generation/", views.text_generation_view, name='text-generation'),
    path('ner/', views.ner_view, name='ner'),
]
