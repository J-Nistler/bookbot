def count_words (corpus):
    word_count = 0
    word_count = len(corpus.split())
    return f"{word_count} words found in the document"