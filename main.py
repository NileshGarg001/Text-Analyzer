import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter


def getFile(path):
    print(path)
    try:
        file = open(path, "r")
        data = file.read()
        file.close()
        return data
    except:
        print("Could not read the file")
        exit()


def topwords(wordlist, n):
    c = Counter(wordlist)
    if n < len(c):
        frqcount = c.most_common(n)
        for a in frqcount:
            print(f"{a[0]} repeated {a[1]} times")
    else:
        print("Not Enough Words")
    return len(c)


def refineWords(text):
    data = re.sub("[^a-zA-Z]", ' ', text)
    data = data.split()
    wordnet = WordNetLemmatizer()
    data = [wordnet.lemmatize(i) for i in data if i not in stopwords.words("English")]
    print(len(data))
    return data


def calculateavg(words):
    sum1 = 0
    for i in range(len(words)):
        sum1 += len(words[i])
    return sum1/len(words)


def main():
    print("Welcome to Word Count Analyzer")
    p = input("Kindly enter the name of text file you want to analyze : ")
    words = getFile(p)
    refined = refineWords(words)
    no = int(input("How many most frequent words do you want to see ?"))
    t = topwords(refined, no)
    print(f"There are {t} unique words in the file other than stopwords (is, am, and...)")
    print(f"Average word length : {calculateavg(refined)} characters")


if __name__ == '__main__':
    main()
