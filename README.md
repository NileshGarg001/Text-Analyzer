# Text Analyzer

## Overview
The Text Analyzer is a Python program designed to analyze text files provided by the user. It performs various operations on the text, such as removing punctuation and stop words, calculating word frequency, determining the number of unique words, and calculating the average word length.

## Features
- Removes punctuation: The program eliminates punctuation marks from the text, allowing for more accurate analysis of word frequency and length.
- Removes stop words: Common stop words, such as "the," "and," and "is," are filtered out to focus on the more significant words in the text.
- Word frequency analysis: The program calculates and displays the most frequent `n` words in the text, where `n` is a user-defined value.
- Unique word count: The program counts the number of unique words in the text, providing insights into the text's vocabulary richness.
- Average word length: The program calculates the average length of words in the text, offering a metric for word complexity or simplicity.

## Usage
1. Run the program by executing the Python script.
2. Provide the file path of the text file you want to analyze.
3. Enter the desired value of `n` to determine the number of most frequent words to display.
4. The program will process the text and generate the analysis results, including the most frequent words, the number of unique words, and the average word length.

## Dependencies
The program relies on the following Python libraries:
- `nltk`: Used for tokenization and stop word removal.
- `string`: Provides a set of punctuation characters for filtering.

Make sure these libraries are installed before running the program. You can install them using pip, like this:
```
pip install nltk
```

## Limitations
- The program assumes that the text file provided by the user is in a readable format. It will not return any data for non tecxt based file.
- The program currently only supports ASCII text files. Support for other text encodings can be added by modifying the code accordingly.
- The accuracy of word frequency analysis and average word length calculation may vary based on the complexity of the text and the presence of unusual word formations.

Feel free to enhance the program with additional features or improvements to overcome these limitations.

## Examples
Here are some examples of how the program can be used:

```
Enter the file path: path/to/your/file.txt
Enter the value of 'n' for most frequent words: 10

---- Text Analysis Results ----
Most frequent words:
1. word1 - 50 occurrences
2. word2 - 42 occurrences
3. word3 - 36 occurrences
4. word4 - 30 occurrences
5. word5 - 25 occurrences
6. word6 - 22 occurrences
7. word7 - 18 occurrences
8. word8 - 15 occurrences
9. word9 - 12 occurrences
10. word10 - 10 occurrences

Number of unique words: 500

Average word length: 5.2
```

## Conclusion
The Text Analyzer program provides a convenient way to analyze text files by extracting meaningful information such as word frequency, unique word count, and average word length. By refining the data and removing unnecessary elements, the program offers valuable insights into the text's characteristics and complexity. Feel free to use, modify, and build upon this program for your own text analysis needs.

Enjoy analyzing your text files with the Text Analyzer!
