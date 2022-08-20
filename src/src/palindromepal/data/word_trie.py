import pickle

import encodings.punycode
import logging
import re
import string
from typing import Iterator

import datrie

from palindromepal.data import words_iterator, get_palindrome_trie_pickle_path

log = logging.getLogger(__name__)


def clean_word(word:str) -> str:
    parts = re.findall("\w+", word)
    if parts:
        return "".join(parts).lower()
    raise RuntimeError(f"Cannot clean {word}")


def build_word_trie(words: Iterator[str]) -> datrie.Trie:
    root = datrie.Trie(alphabet=string.ascii_lowercase)
    for word in words:
        root[clean_word(word)] = word
    return root


def find_key_combinations(big_key, word_table)->Iterator[tuple]:
    if big_key:
        for prefix in word_table.prefixes(big_key):
            if prefix in word_table:
                remander = big_key[len(prefix):]
                for combo in find_key_combinations(remander, word_table):
                    yield (prefix,) + combo
    else:
        yield ()


def find_valid_subkeys(key, word_trie, max_length=3)->Iterator[tuple]:

    for key_combo in find_key_combinations(key, word_trie):
        if len(key_combo) <= max_length:
            yield key_combo

def build_palindrome_trie(word_trie:datrie, max_word_length=14)->datrie.Trie:
    palindrome_trie = datrie.Trie(alphabet=string.ascii_lowercase)
    for key, word in word_trie.items():
        if len(key) <= max_word_length:
            inverted_key = key[::-1]
            for key_combo in find_valid_subkeys(inverted_key, word_trie):
                palindrome_trie.setdefault(key, set()).add(key_combo)
        else:
            log.info(f"Skipping {word}, it is too long!")

    return palindrome_trie


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    word_trie = build_word_trie(words_iterator())
    palindrome_trie = build_palindrome_trie(word_trie)

    for k, v in palindrome_trie.items():
        print(f"{k} -> {v}")

    with get_palindrome_trie_pickle_path().open("wb") as f:
        pickle.dump(palindrome_trie, f)

