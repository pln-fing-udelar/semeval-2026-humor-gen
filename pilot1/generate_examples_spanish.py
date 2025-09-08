#!/usr/bin/env python
import json
import random
import os

NUM_OUTPUTS = 100
NUM_CONDITIONS = 3
PATH_SPANISH = '../spanish'

def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file]


def main() -> None:
    words = read_lines(os.path.join(PATH_SPANISH,"words_es.txt"))
    topics = read_lines(os.path.join(PATH_SPANISH,"topics_es.txt"))
    styles = read_lines(os.path.join(PATH_SPANISH,"styles_es.txt"))

    for _ in range(NUM_OUTPUTS):
        words_copy = list(words)
        random.shuffle(words_copy)

        topics_copy = list(topics)
        random.shuffle(topics_copy)

        styles_copy = list(styles)
        random.shuffle(styles_copy)

        # We can have the "words" condition multiple times.
        # Using the same list and popping ensure we don't repeat the same word in a single output.
        list_of_lists = [
            ("word", words_copy),
            ("word", words_copy),
            ("word", words_copy),
            ("topic", topics_copy),
            ("style", styles_copy),
        ]
        random.shuffle(list_of_lists)

        conditions = []

        for _ in range(NUM_CONDITIONS):
            type_, sampled_list = list_of_lists.pop()
            sampled_value = sampled_list.pop()
            conditions.append({"type": type_, "value": sampled_value})

        print(json.dumps(conditions, ensure_ascii=False))


if __name__ == "__main__":
    main()
