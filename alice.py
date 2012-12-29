#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.

from string import punctuation
from random import choice, randint


class Text(object):
    def __init__(self, text):
        self.text = text
        self.all_words = [] 
        self.word_frequency = {} #{word: count}  
        self.second_words = {} #{word: [follower, follower]
        self.end_words = {} #{bareword: punct}
        self.distribution = {}
        self.my_biagrams = {}

    def PrepareData(self):
        words = self.text.lower().replace('--', ' ').split()
        prev = words[0].strip(punctuation)
        self.all_words.append(prev)
        self.word_frequency[prev] = 1
        self.second_words[prev] = []
        for word2 in words[1:]:
            word = word2.strip(punctuation)
            word2 = word2.lstrip(punctuation)
            word2 = word2.rstrip(
            ''.join([c for c in punctuation if c in punctuation if c not in '.!?']))
            if word:
                self.all_words.append(word)
                if word in self.word_frequency:
                    self.word_frequency[word] += 1
                else:
                    self.word_frequency[word] = 1
                    if word not in self.second_words and word == word2:
                        self.second_words[word] = []
                if prev in self.second_words:
                    self.second_words[prev].append(word2)
                if word != word2:
                    if word in self.end_words:
                        self.end_words[word].append(word2[-1])
                    else:
                        self.end_words[word] = [word2[-1]]
                prev = word
        
    def GetUniqueWords(self):
        return list(self.second_words.keys())
        
    def GetAllWords(self):
        return self.all_words
        
    def GetSecondWords(self):
        return self.second_words
        
    def GetWordFreq(self):
        return self.word_frequency
        
    def Freq(self, my_dict, type, top=10):
        if type == 'most':
            a = sorted(list(my_dict.values()))[-top:]
        elif type == 'least':
            a = sorted(list(my_dict.values()))[:top]
        words = []
        for word in my_dict.keys():
            if my_dict[word] in a:
                words.append(word)
        return words[:top]
    
    def GenerateText(self, sentences):
        generated = ''
        for _ in range(sentences):
            word = choice(self.all_words)
            generated += word[0].upper() + word[1:]
            k = 0
            while (generated[-1] not in '.!?' and word not in self.end_words) or k < 3:
                if word in self.second_words:
                    word = choice(self.second_words[word])
                    generated += ' ' + word
                else:
                    word = choice(self.all_words)
                k += 1
            if generated[-1] not in punctuation:
                generated += choice(self.end_words[word])
            generated += ' '
        return generated[:-1]
        
    def GenerateText2(self, sentences):
        d = {}
        generated = ''
        text = self.text
        for i in ['.', ',', '!', '?', ':']:
            text = text.replace(i, ' ' + i)
        for i in ['"']:
            text = text.replace(i, i + ' ')
        text = text.split()
        for i in range(len(text) - 1):
            if text[i] in d:
                d[text[i]].append(text[i + 1])
            else:
                d[text[i]] = [text[i + 1]]
        i = 0
        word = choice(d['.'])
        generated += word[0].upper() + word[1:]
        while i < sentences:
            word = choice(d[word])
            generated += ' ' + word
            if word in ('.', '?', '!', '...'):
                i += 1
            
            
        
        return generated
        
        
    def Palindrome(self):
        words = self.GetUniqueWords()
        return [w for w in words if w == w[::-1] and len(w) > 1]
        
    def DistributionLength(self):
        for word, count in self.word_frequency.items():
            if len(word) in self.distribution:
                self.distribution[len(word)] += count
            else:
                self.distribution[len(word)] = count
        return self.distribution
        
    def DistributionULength(self):
        for word in self.word_frequency.keys():
            if len(word) in self.distribution:
                self.distribution[len(word)] += 1
            else:
                self.distribution[len(word)] = 1
        return self.distribution
        
    def DistributionFreq(self):
        for amt in self.word_frequency.values():
            if amt in self.distribution:
                self.distribution[amt] += 1
            else:
                self.distribution[amt] = 1
        return self.distribution
    
    def Bigrams(self, text):
        i = 0
        while i < len(text) - 1:
            bigram = '{0} {1}'.format(text[i], text[i + 1])
            if bigram in self.my_bigrams:
                self.my_bigrams[bigram] = self.my_bigrams[bigram] + 1
                i += 1
            else:
                self.my_bigrams[bigram] = 1
                i += 1
        return self.my_bigrams
      
