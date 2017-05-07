import numpy as np
import matplotlib.pyplot as plt
import os

def make_bookmap(book_text):
    book_map = []
    longest_line = 0
    line_map = book_text.split('.')

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

def numpy_image_maker(book_map, book_name):
    a = np.asarray(book_map)
    a = np.transpose(a)
    plt.axis('off')
    plt.imshow(a, cmap='plasma' ,interpolation='nearest')
    # plt.show()
    plt.savefig(book_name + '_map_image.png', bbox_inches='tight')

# Create a file with a matrix suitable for Octave/MATLAB
def matrix_maker(book_map, book_name):
    a = np.asarray(book_map)
    a = np.transpose(a)
    np.savetxt(book_name + ".mat", a, newline=";\n")

make_image = True
make_matrix = False

def main():
    book_name, ext = os.path.splitext('the_last_question.txt')
    with open(book_name + ext, 'r') as f:
        book_text = f.read()

    book_map, longest_line = make_bookmap(book_text)
    pad_with_zeroes(book_map, longest_line)

    if make_image:
        numpy_image_maker(book_map, book_name)
    if make_matrix:
        matrix_maker(book_map, book_name)


if __name__ == "__main__":
    main()