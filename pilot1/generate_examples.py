#!/usr/bin/env python
import json
import random

NUM_OUTPUTS = 100
NUM_CONDITIONS = 3


def read_lines(path: str) -> list[str]:
    with open(path) as file:
        return [line.strip() for line in file]


def main() -> None:
    words = read_lines("words.txt")
    topics = read_lines("topics.txt")
    styles = read_lines("styles.txt")

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

        print(json.dumps(conditions))


if __name__ == "__main__":
    main()
