#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.

from string import punctuation
from random import choice, randint


all_words = [] 
word_frequency = {} #{word: count}  
second_words = {} #{word: [follower, follower]
end_words = {} #{bareword: punct}
distribution = {}

def PrepareData(text):
    words = text.lower().replace('--', ' ').split()
    prev = words[0].strip(punctuation)
    all_words.append(prev)
    word_frequency[prev] = 1
    second_words[prev] = []
    for word2 in words[1:]:
        word = word2.strip(punctuation)
        word2 = word2.lstrip(punctuation)
        word2 = word2.rstrip(
        ''.join([c for c in punctuation if c in punctuation if c not in '.!?']))
        if word:
            all_words.append(word)
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
                if word not in second_words and word == word2:
                    second_words[word] = []
            if prev in second_words:
                second_words[prev].append(word2)
            if word != word2:
                if word in end_words:
                    end_words[word].append(word2[-1])
                else:
                    end_words[word] = [word2[-1]]
            prev = word
    
def GetUniqueWords():
    return second_words.keys()
    
def GetAllWords():
    return all_words
    
def GetSecondWords():
    return second_words
    
def GetWordFreq():
    return word_frequency
    
def Freq(text, type, top=10):
    if type == 'most':
        a = sorted(list(text.values()))[-top:]
    elif type == 'least':
        a = sorted(list(text.values()))[:top]
    words = []
    for word, times in text.items():
        if text[word] in a:
            words.append(word)
    return words[:top]


def GenerateText(sentences):
    generated = ''
    for _ in range(sentences):
        word = choice(all_words)
        generated += word[0].upper() + word[1:]
        k = 0
        while (generated[-1] not in '.!?' and word not in end_words) or k < 3:
            if word in second_words:
                word = choice(second_words[word])
                generated += ' ' + word
            else:
                word = choice(all_words)
            k += 1
        if generated[-1] not in punctuation:
            generated += choice(end_words[word])
        generated += ' '
    return generated[:-1]
    
def Palindrome():
    return [w for w in GetUniqueWords() if w == w[::-1] and len(w) > 1]
    
def DistributionLength():
    for word, count in word_frequency.items():
        if len(word) in distribution:
            distribution[len(word)] += count
        else:
            distribution[len(word)] = count
    return distribution
    
def DistributionULength():
    for word in word_frequency.keys():
        if len(word) in distribution:
            distribution[len(word)] += 1
        else:
            distribution[len(word)] = 1
    return distribution
    
def DistributionFreq():
    for amt in word_frequency.values():
        if amt in distribution:
            distribution[amt] += 1
        else:
            distribution[amt] = 1
    return distribution

def Bigrams(text):
    my_bigrams = {}
    i = 0
    while i < len(text) - 1:
        bigram = '{0} {1}'.format(text[i], text[i + 1])
        if bigram in my_bigrams:
            my_bigrams[bigram] = my_bigrams[bigram] + 1
            i += 1
        else:
            my_bigrams[bigram] = 1
            i += 1
    return my_bigrams
  


if __name__ == '__main__':
  main()
