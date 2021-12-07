def check_data(lst_coefs, lst_words):
    if not isinstance(lst_words, list) or not isinstance(lst_coefs, list):
        print('-1')
        return False
    elif not all(isinstance(word, str) for word in lst_words):
        print('-1')
        return False
    elif not all(isinstance(nb, float) for nb in lst_coefs):
        print('-1')
        return False
    elif not len(lst_words) == len(lst_coefs):
        print('-1')
        return False
    return True


class Evaluator():

    def zip_evaluate(lst_coefs, lst_words):
        if not check_data(lst_coefs, lst_words):
            return
        count = 0
        for word, nb in zip(lst_words, lst_coefs):
            count += len(word) * nb
        print(count)

    def enumerate_evaluate(lst_coefs, lst_words):
        if not check_data(lst_coefs, lst_words):
            return
        count = 0
        for i, word in enumerate(lst_words):
            count += len(word) * lst_coefs[i]
        print(count)


if __name__ == '__main__':
    word = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

    Evaluator.zip_evaluate(coefs, word)

    Evaluator.enumerate_evaluate(None, None)
    Evaluator.enumerate_evaluate([1, 2, 3], [])
    Evaluator.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"])
    Evaluator.enumerate_evaluate(coefs, word)
