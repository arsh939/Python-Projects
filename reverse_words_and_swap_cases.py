def reverse_words_order_and_swap_cases(sentence):
    arrSen = sentence.split()
    arrSen = list(reversed(arrSen))
    result = list(" ".join(arrSen))
    for i in range(len(result)):
        if result[i].isupper():
            result[i] = result[i].lower()
        else:
            result[i] = result[i].upper()

    return "".join(result)


res = reverse_words_order_and_swap_cases("aWESOME is cODING")
print(res)

