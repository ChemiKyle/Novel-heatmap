import numpy as np
import matplotlib.pyplot as plt
import os, tkinter, re


def make_bookmap(book_text):
    book_map = []
    longest_line = 0
    line_map = re.split('[\.\?\!]', book_text)

    for line in line_map[:-1]: # Skip the last entry since it's a space after the final period
        this_line_map = line.replace('"', '').replace(',','').replace(';','').replace("\n",'').split(' ')
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

def pad_vector_with_zeroes(book_map, longest_line):
    for line in book_map:
        word_count = len(line)
        if word_count < longest_line:
            for i in range(longest_line - word_count):
                line.append(0)

directly_to_figure = True # Set to false to produce a preview first
def numpy_image_maker(book_map, book_name):
    a = np.asarray(book_map)
    a = np.transpose(a)
    plt.axis('off')
    cmap = 'Blues_r'
    dpi = 100 # Default for this with direct write is 80, but images our size don't warrant compression
    plt.imshow(a, cmap=cmap ,interpolation='nearest')
    if directly_to_figure:
        plt.savefig(book_name + '_map_image.png', bbox_inches='tight', dpi=dpi)
    else:
        plt.show()


# Create a file with a matrix suitable for Octave/MATLAB
make_matrix = False
def matrix_maker(book_map, book_name):
    a = np.asarray(book_map)
    a = np.transpose(a)
    np.savetxt(book_name + ".mat", a, newline=";\n")

def process_to_dictionary(chosen_file, chapter_dict):
    book_name, ext = os.path.splitext(chosen_file)
    with open(chosen_file, 'r') as f:
        book_text = f.read()

    book_map, longest_line = make_bookmap(book_text)
    chapter_dict[book_name] = book_map
    pad_vector_with_zeroes(book_map, longest_line)

make_image = True # Determines whether or not to plot the result

def process_chapters_to_images(chapter_dict):
    for i in chapter_dict:
        file_name = i
        book_map = chapter_dict[i]
        numpy_image_maker(book_map, file_name)

# Make a vector full of zeroes the size of the longest sentence, used to pad width
def make_blank_pad_vector(longest_line):
    pad_vector = []
    for i in range(longest_line):
        pad_vector.append(0)
    return pad_vector

normalizing = True
def normalize_all_maps(chapter_dict):
    longest_sentence = 0
    most_sentences = 0
    for i in chapter_dict:
        this_sentence_count = len(chapter_dict[i])
        if this_sentence_count > most_sentences:
            most_sentences = this_sentence_count
        this_longest_sentence = len(chapter_dict[i][0])
        if this_longest_sentence > longest_sentence:
            longest_sentence = this_longest_sentence

    # pad_vector = make_blank_pad_vector(longest_sentence)
    for i in chapter_dict:
        pad_vector_with_zeroes(chapter_dict[i], longest_sentence) # Normalizes blank space to largest sentence (vertical)
        # this_sentence_count = len(chapter_dict[i])
        # for i in range(most_sentences - this_sentence_count):
        #     chapter_dict[i].append(pad_vector)


def main():
    chapter_dict = {}
    file_list = tkinter.filedialog.askopenfilenames() # Supports processing multiple files sequentially

    for chosen_file in file_list:
        process_to_dictionary(chosen_file, chapter_dict)

    if normalizing:
        normalize_all_maps(chapter_dict)
    if make_image:
        process_chapters_to_images(chapter_dict)

if __name__ == "__main__":
    main()