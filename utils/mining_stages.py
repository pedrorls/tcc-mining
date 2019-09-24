import re, unidecode, nltk, PyPDF2
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


from .text_extractor import pdf_to_text


def remove_noise(text):
    return "".join(re.sub(r"(\d+)|(\.)|(\/)", " / ", sentence) for sentence in text)


def remove_accents(bag_of_words):
    return map(unidecode.unidecode, bag_of_words)


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
            "area",
            "subarea",
            "ingles",
            "portugues",
            "espanhol",
            "idiomas",
            "especialidade",
        ]
    )
    return [word for word in bag_of_words if not word in stop_words]


def text_processing(file):
    text = pdf_to_text(file)
    tokens = sent_tokenize(text.lower())
    tokens = filter_by_areas(tokens)
    tokens = remove_noise(tokens)
    tokens = word_tokenize(tokens)
    tokens = remove_accents(tokens)
    tokens = remove_stopwords(tokens)
    text_size = len(tokens)
    tokens = lemma(tokens)
    # bigramns_tokens = [" ".join(pair) for pair in nltk.bigrams(tokens)]
    tokens_freq = FreqDist(tokens)

    bag_of_words = []
    for token in tokens_freq.most_common():
        relative_frequency = round((token[1] / text_size) * 100, 2)
        bag_of_words.append(
            {
                "word": token[0],
                "frequency": token[1],
                "relative_frequency": relative_frequency,
            }
        )

    return bag_of_words
