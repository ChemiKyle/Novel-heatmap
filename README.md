## Novel Heatmap  
![light](/images/the_last_question_map_image.png?raw=true "Isaac Asimov's The Last Question")
Image created from Isaac Asimov's _The Last Question_.

# How it works
Creates a heatmap of the words in a book from a .txt file, image output looks somewhat like a skyline. This works by making a matrix of the sentences in the input file(s); each sentence is a vector and each number corresponds to the length of the word at its corresponding position.  
i.e.: "The quick brown fox jumped over the lazy dog" becomes [3 5 5 3 6 4 3 4 3] and is represented thusly  
![fox](/images/fox_map_image.png?raw=true "Example vector")

# Workflow
The images can be made by running `book_map.py` and selecting file(s) via a tkinter GUI; there are various options within the code for things like "normalizing" the data when processing multiple files and outputting `.mat` files for use with other programs such as Octave.   
To convert an `.epub` book to a `.txt` file, you can use the `ebook-convert` command in terminal if you have Calibre installed.  
Creating an image works best with single chapters, so I also wrote a script to help convert the output of `ebook-convert` into smaller files, the delimiter is currently the string "Chapter ", so it will likely need some cleaning up if it works at all.  
For \*nix users, `autotrim.sh` can be used to remove whitespace from all images.

# Normalization
Multiple chapters (files) are "normalized" by adding 0's to the end of vectors until they match the length of the longest sentence. Each chapter is then normalized by length by adding 0 filled vectors until all matrices are the same size.
