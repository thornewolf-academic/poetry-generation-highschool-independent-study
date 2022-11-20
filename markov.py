import random
from collections import defaultdict


def tokenize(text):
    """Convert text into a list of words."""
    text = text.lower()
    return text.split()


def generate_frequency_dictionary_from_text(text, input_length=2):
    """Generate a frequency dictionary from a text."""
    freq_dict = defaultdict(list)
    words = tokenize(text)
    for i in range(len(words) - input_length):
        key = tuple(words[i : i + input_length])
        value = words[i + input_length]
        freq_dict[key].append(value)
    return freq_dict


def infer_next_word(freq_dict, input_words):
    """Infer the next word from the input words."""
    key = tuple(input_words[-len([*freq_dict.keys()][0]) :])
    return random.choice(freq_dict[key])


def inferer_next_n_words(freq_dict, input_words, n=10):
    """Infer the next n words from the input words."""
    words = input_words
    for _ in range(n):
        words.append(infer_next_word(freq_dict, words))
    return words


if __name__ == "__main__":
    ...
