def words_order(text, words):
    return words == [w for w in text.split() if w in words and words.count(w) < 2]