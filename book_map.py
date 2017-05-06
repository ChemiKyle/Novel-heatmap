

test_sentence = "This is a sentence. So is this one. This one's short. But this one is very long, the longest of them all."

def make_bookmap(sentence):
    book_map = []
    longest_line = 0
    line_map = sentence.split('.')

    for line in line_map:
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

# def pad_with_zeroes(book_map)

book_map, longest_line = make_bookmap(test_sentence)

print(book_map)