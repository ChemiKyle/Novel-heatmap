## Novel Heatmap

Creates a heatmap of the words in a book from a .txt file, image output looks somewhat like a skyline. Works by making a matrix of the number of characters in each words in a sentence, each number corresponds to the length of the word at its corresponding position.  
i.e.: "The quick brown fox jumped over the lazy dog" becomes [3 5 5 3 6 4 3 4 3] and is represented thusly  
![The quick brown fox jumped over the lazy dog](/fox_map_image.png?raw=true)



To convert an `.epub` book to a `.txt` file, you can use Calibre's `ebook-convert` command. Works best with single chapters.