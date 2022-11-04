from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

from nlpclassification.models import NameForm, FillMask
from nlpclassification.nlp_models import question_answering_model, fill_mask_model, summarization_model, \
    sentiment_analysis, zero_shot_classification_model


# Create your views here.

def index(request):
    return render(request, 'nlpclassification/index.html')


def question_answering(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            question = form.cleaned_data['question']
            sentence = form.cleaned_data['sentence']
            a = question_answering_model(question, sentence)
            # TODO improve the % module
            # if a['score']*100 < 30:
            #     a['answer'] = "Machine is not able to find the answer from the given sentence"
            return render(request, 'nlpclassification/question_answering.html', {'form': a['answer']})
    else:
        return render(request, 'nlpclassification/question_answering.html')


def masked_word(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FillMask(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            sentence = form.cleaned_data['sentence']
            a = fill_mask_model(sentence, top_k=20)
            return render(request, 'nlpclassification/fill_mask.html', {'form': a})
    else:
        return render(request, 'nlpclassification/fill_mask.html')


def summarization(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FillMask(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as requiredsentiment_analysis
            # ...
            # redirect to a new URL:
            sentence = form.cleaned_data['sentence']
            a = summarization_model(sentence)
            return render(request, 'nlpclassification/summarization.html', {'form': a})
    else:
        return render(request, 'nlpclassification/summarization.html')


def sentiment_analysis_view(request):
    if request.method == 'POST':
        form = FillMask(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            a = sentiment_analysis(sentence)
            return render(request, 'nlpclassification/sentiment_analysis.html', {'form': a})
        else:
            print("fprm invalid")
    else:
        return render(request, 'nlpclassification/sentiment_analysis.html')
