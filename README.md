## Novel Heatmap  
Create a heatmap of the words in a book from any text, like this image:  
![Letters from Saint-Paul](/images/starry_night.png "Letters from Saint-Paul")  
which was synthesized from the text of [this article about Vincent van Gogh.](https://www.moma.org/learn/moma_learning/vincent-van-gogh-the-starry-night-1889)

# How does it work?
![light](/images/the_last_question_map_image.png?raw=true "Isaac Asimov's The Last Question")
(Image created from Isaac Asimov's _The Last Question_.)  

It works by making a matrix of the sentences in the input file(s); each sentence is a vector and each number corresponds to the length of the word at its corresponding position.  
i.e.: "The quick brown fox jumped over the lazy dog" becomes [3 5 5 3 6 4 3 4 3] and is represented thusly  
![fox](/images/fox_map_image.png?raw=true "Example vector")  
Processing a .txt file containing `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque laoreet convallis leo vitae dignissim. Nam et metus bibendum, scelerisque ex vel, rhoncus tortor.` would produce the following result:  
![lore_impsum](/images/lorem_ipsum_example_map_image.png)  
A paragraph of lorem ipsum would be presented:  
![lorem_paragraph](/images/lorem_paragraph.png)


# Workflow
The images can be made by running `book_map.py` and selecting your file(s) via a tkinter GUI; there are various options within the code for things like "normalizing" the data when processing multiple files and outputting `.mat` files for use with other programs such as Octave.

To convert an `.epub` or similar format book to a `.txt` file, you can use the `ebook-convert` command in terminal if you have [Calibre](https://calibre-ebook.com/) installed.  
I think creating an image from a book works best by combining separate images for each chapter, so I also wrote a script to help split up the output of `ebook-convert` into distinct files for each chapter, the delimiter is currently the string "Chapter ", so it will likely need some cleaning up if it works at all.  
For \*nix users, `autotrim.sh` can be used to remove whitespace from all images within the directory it's called from.

# Normalization
Multiple chapters (files) are "normalized" by adding 0's to the end of vectors until they match the length of the longest sentence. Each chapter is then normalized by length by adding 0 filled vectors until all matrices are the same size.  
If you're not worried about visualizing data and just want pretty pictures, turning off normalization and experimenting with the files can produce some nice images. Below is a comparison of a somewhat extreme example from processing and combining the first 5 chapters of Tolstoy's _What is Art?_ - which conveniently has a sentence-rich third chapter - with (left or top) and without (right or bottom) normalization.  
![normalized](/images/what_is_art_normalized.png "normalized")
![raw](/images/what_is_art_raw.png "raw")  
(NB: These are not fully automated; both images were made by importing individual chapter images into inkscape, stacking and center aligning them. For the raw image I manually changed the color of the area outside of each respective matrix to match the color scheme to demonstrate the aesthetic intent of that setting.)
