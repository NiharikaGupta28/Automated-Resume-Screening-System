import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Tokenization
    tokens = word_tokenize(text)

    # Stopword removal
    stop_words = set(stopwords.words('english'))

    filtered_tokens = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            filtered_tokens.append(word)

    # Lemmatization
    lemmatizer = WordNetLemmatizer()

    cleaned_tokens = []

    for word in filtered_tokens:
        cleaned_tokens.append(lemmatizer.lemmatize(word))

    return cleaned_tokens


if __name__ == "__main__":

    sample_text = """
    John has worked on Machine Learning projects
    and is skilled in Python and SQL.
    """

    result = preprocess_text(sample_text)

    print(result)