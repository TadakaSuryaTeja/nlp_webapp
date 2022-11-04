from transformers import pipeline


def question_answering_model(question, sentence):
    model_name = "deepset/roberta-base-squad2"
    question_answer = pipeline("question-answering", model=model_name, tokenizer=model_name)
    a = question_answer(question=question,
                        context=sentence)
    return a


def zero_shot_classification_model(candidate_labels: list[str], sentence):
    classifier = pipeline("zero-shot-classification")
    result = classifier(sentence, candidate_labels=candidate_labels)
    return result


def text_generation_model(sentence: str, max_length=30, num_return_sequences=3):
    generator = pipeline("text-generation", model="distilgpt2")
    result = generator(sentence,
                       max_length=max_length,
                       num_return_sequences=num_return_sequences)
    return result['generated_text']


def fill_mask_model(sentence: str = "This course will teach you all about <mask> models.", top_k=2):
    """
    This course will teach you all about <mask> models.
    """
    unmasker = pipeline("fill-mask")
    result = unmasker(sentence, top_k=top_k)
    return result


def named_entity_recognition_model(sentence: str):
    ner = pipeline("ner", grouped_entities=True)
    result = ner(sentence)
    return result


def summarization_model(sentence: str):
    summarizer = pipeline("summarization")
    result = summarizer(sentence)
    return result


def translation_model(sentence):
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    result = translator(sentence)
    return result


def sentiment_analysis(sentence: str):
    classifier = pipeline("sentiment-analysis")
    result = classifier(sentence)
    return result
