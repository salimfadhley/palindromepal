from palindromepal.data.word_trie import clean_word


def test_clean_word1():
    assert clean_word('Abc') == 'abc'

def test_clean_word2():
    assert clean_word('A.bc') == 'abc'