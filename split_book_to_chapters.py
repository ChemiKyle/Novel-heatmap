import tkinter


def split_by_chapter(book_file):
    chapter_split = book_file.split('Chapter ')  # Obviously not perfect, but works in many cases
    return chapter_split


def write_chapters_to_files(chapter_split):
    chap_num = 0
    for i in chapter_split:
        with open('ch' + str(chap_num) + '.txt', 'w') as w:
            w.write(i)
        chap_num += 1


def main():
    chosen_book_file = tkinter.filedialog.askopenfilename()
    with open(chosen_book_file, 'r') as r:
        book_file = r.read()

    chapter_split = split_by_chapter(book_file)
    write_chapters_to_files(chapter_split)


if __name__ == '__main__':
    main()
