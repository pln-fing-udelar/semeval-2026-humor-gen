#!/usr/bin/env python
import json
import random
import os

NUM_OUTPUTS_PER_IMAGE = 2
NUM_EXTRA_CONDITIONS = 2


def read_lines(path: str) -> list[str]:
    with open(path) as file:
        return [line.strip() for line in file]

def read_file_names(path: str) -> list[str]:
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def main() -> None:
    words = read_lines("words.txt")
    topics = read_lines("topics.txt")
    images = read_file_names("../images")

    # Each image appears twice with different conditions
    for image in images:
        for _ in range(NUM_OUTPUTS_PER_IMAGE):
            words_copy = list(words)
            random.shuffle(words_copy)

            topics_copy = list(topics)
            random.shuffle(topics_copy)

            # We can have the "words" condition multiple times.
            # Using the same list and popping ensure we don't repeat the same word in a single output.
            list_of_lists = [
                ("word", words_copy),
                ("word", words_copy),
                ("topic", topics_copy),
            ]
            random.shuffle(list_of_lists)

            conditions = [{"type": "image", "value": image}]

            for _ in range(NUM_EXTRA_CONDITIONS):
                type_, sampled_list = list_of_lists.pop()
                sampled_value = sampled_list.pop()
                conditions.append({"type": type_, "value": sampled_value})

            print(json.dumps(conditions))


if __name__ == "__main__":
    main()
