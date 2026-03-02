def words_order(text: str, words: list) -> bool:
    liste = [text.split().index(word) if text.split().count(word) >= 1 else -1 for word in words ]
    return liste == sorted(liste) if (len(set(liste)) > 1 and len(words) > 1 or len(words) == 1) and -1 not in liste else False