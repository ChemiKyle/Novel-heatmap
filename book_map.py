import numpy as np
import matplotlib.pyplot as plt
import os

def make_bookmap(sentence):
    book_map = []
    longest_line = 0
    line_map = sentence.split('.')

    for line in line_map[:-1]: # Skip the last entry since it's a space after the final period
        this_line_map = line.split(' ')
        line_count_map = []

        for word in this_line_map:
            wordlength = len(word)
            if wordlength > 0:
                line_count_map.append(wordlength)
        this_line_map_size = len(line_count_map)
        if this_line_map_size > 0:
            book_map.append(line_count_map)
            if this_line_map_size > longest_line:
                longest_line = this_line_map_size

    return book_map, longest_line

def pad_with_zeroes(book_map, longest_line):
    for line in book_map:
        word_count = len(line)
        if word_count < longest_line:
            for i in range(longest_line - word_count):
                line.append(0)

def main():
    book_name, ext = os.path.splitext('the_last_question.txt')
    with open(book_name + ext, 'r') as f:
        test_sentence = f.read()

    book_map, longest_line = make_bookmap(test_sentence)
    pad_with_zeroes(book_map, longest_line)
    a = np.asarray(book_map)
    a = np.transpose(a)
    plt.imshow(a, cmap='plasma' ,interpolation='nearest')
    plt.savefig(book_name + '_map_image.png', bbox_inches='tight')

if __name__ == "__main__":
    main()