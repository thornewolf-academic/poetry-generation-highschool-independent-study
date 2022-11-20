import random
from markov import (
    generate_frequency_dictionary_from_text,
    inferer_next_n_words,
    infer_next_word,
)
from sonnet_downloader import fetch_local_sonnets

FULL_STOPS = ".?!;:"


def full_stop_in_word_list(word_list):
    result = any(fs in word for fs in FULL_STOPS for word in word_list)
    return result


def get_stop_odds(words_per_line, start, end):
    if end - start < words_per_line:
        return 0
    odds = (-words_per_line + (end - start - 1)) * 1 / 3
    return odds


def generate_poem(seed=None, lines=10, words_per_line=10):
    sonnets = fetch_local_sonnets()
    f = generate_frequency_dictionary_from_text(sonnets)
    if seed is None:
        seed = list(random.choice([*f.keys()]))
    state = seed
    words = inferer_next_n_words(f, state, lines * words_per_line)

    generated_lines = []
    start = 0
    end = 0
    while end < len(words):
        stop_odds = get_stop_odds(words_per_line, start, end)
        if full_stop_in_word_list(words[start:end]) and random.random() < stop_odds:
            generated_lines.append(" ".join(words[start:end]))
            start = end
        else:
            end += 1
    if start != end:
        generated_lines.append(" ".join(words[start:end]))

    return "\n".join(generated_lines)


