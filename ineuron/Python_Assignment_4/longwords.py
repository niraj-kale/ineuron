def filter_long_words(words, n):
    lwords = []
    for word in words:
        if len(word) > n:
            lwords.append(word)
    return lwords


words = ['adbf', 'sdfsdwsdfsdf', 'sdfdsf2333ddd', 'sdfsdfdsfsdf']

print(filter_long_words(words,5))