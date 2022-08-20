import itertools
from pathlib import Path
from typing import Iterator

import pkg_resources



def get_words_file_path()->Path:
    return Path(pkg_resources.resource_filename(__name__, "words.txt"))

def get_palindrome_trie_pickle_path()->Path:
    return Path(pkg_resources.resource_filename(__name__, "palindrome_trie.pickle"))

def words_iterator()->Iterator[str]:
    with get_words_file_path().open() as f:
        for line in f:
            yield line.strip()

if __name__ == "__main__":
    for word in itertools.islice(words_iterator(),50):
        print(word)
