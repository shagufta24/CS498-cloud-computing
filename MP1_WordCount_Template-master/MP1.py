import random 
import os
import string
import sys
import re

# To run the code, use: cat input.txt | python MP1.py <seed>

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def find_top_words(word_list, top_n=20):
    word_frequency = {}

    # Count the frequency of each word in the list
    for word in word_list:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Sort the words by frequency in descending order
    sorted_word_frequencies = sorted(word_frequency.items(), key=lambda x: (-x[1], x[0]))
    sorted_words = [word for word, _ in sorted_word_frequencies]

    # Get the top N words
    top_words = sorted_words[:top_n]
    return top_words

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO

    # Read all lines from stdin
    lines = sys.stdin.readlines()
    
    # Select the lines at selected indexes
    selected_lines = [lines[i] for i in indexes]
    
    all_words = []
    for line in selected_lines:
        # Split each line using delimiters
        words = re.split(f"[{re.escape(delimiters)}]", line)

        # Clean up the words
        for word in words:
            if word.strip() and word.strip().lower() not in stopWordsList:
                clean_word = word.strip().lower().encode('utf-8', 'ignore').decode('utf-8')
                all_words.append(clean_word)

    # Find top frequency words
    ret = find_top_words(all_words, 20)
         
    for word in ret:
        print(word)

process(sys.argv[1])
