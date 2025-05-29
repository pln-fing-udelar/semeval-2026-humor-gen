#!/usr/bin/env bash

head -n 25 nouns.txt > words.txt
head -n 25 verbs.txt >> words.txt
head -n 25 adjectives.txt >> words.txt
head -n 25 adverbs.txt >> words.txt
shuf words.txt -o words.txt
