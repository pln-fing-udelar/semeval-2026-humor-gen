#!/usr/bin/env python
import sys
from nltk.corpus import stopwords

def read_lines(path: str) -> list[str]:
    with open(path) as file:
        return [line.strip() for line in file]

def main(fname: str) -> None:
    en_stopwords = set(stopwords.words('english'))
    words = read_lines(fname)
    for w in words:
        if w not in en_stopwords:
            print(w)

if __name__ == "__main__":
    main(sys.argv[1])
