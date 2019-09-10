import re
import PyPDF2
import nltk
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


from text_extractor import pdf_to_text


def remove_noise(text):
    return "".join(re.sub(r"(\d+)|(\.)|(\/)", " / ", sentence) for sentence in text)


def filter_by_areas(bag_of_sentences):
    return [
        sentence.replace("\n", " ")
        for sentence in bag_of_sentences
        if ("grande área" in sentence)
        or ("subárea" in sentence)
        or ("àrea" in sentence)
    ]


def lemma(bag_of_words):
    word_lemma = WordNetLemmatizer()
    return [word_lemma.lemmatize(word) for word in bag_of_words]


def remove_stopwords(bag_of_words):
    stop_words = set(
        stopwords.words("portuguese")
        + stopwords.words("english")
        + list(punctuation)
        + [
            "grande",
            "área",
            "subárea",
            "inglês",
            "português",
            "espanhol",
            "idiomas",
            "especialidade",
        ]
    )
    return [word for word in bag_of_words if not word in stop_words]


text = pdf_to_text("mozilla.pdf")
tokens = sent_tokenize(text.lower())
tokens = filter_by_areas(tokens)
tokens = remove_noise(tokens)
tokens = word_tokenize(tokens)
tokens = remove_stopwords(tokens)
tokens = lemma(tokens)
pairs = [" ".join(pair) for pair in nltk.bigrams(tokens)]
print(pairs)
pairs_tokens = word_tokenize(pairs)
freq = FreqDist(tokens)
print(freq.most_common())
