def reverse_words_order_and_swap_cases(sentence):
    arrSen = sentence.split()
    arrSen = list(reversed(arrSen))
    
    result = []
    for w in arrSen:
        result.append(w.swapcase())
    return " ".join(result)


res = reverse_words_order_and_swap_cases("aWESOME is cODING")
print(res)

