#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.
  
with open('alice_in_wonderland.txt') as alice_file:
    alice_text = alice_file.read()
    
def GetWords(text):
    newtext = str(text).lower()
    words = []
    word = ''
    for character in newtext + '!':
      if character.isalpha():
        word = word + character
      else:
        words.append(word)
        word=''
    words = [s for s in words if s]
    return words

words = GetWords(alice_text)

def GetUniqueWords(text):
    return set(GetWords(text))
    
def WordsCount(text): 
    my_dict={} 
    for word in text:
        if word not in my_dict:
            my_dict[word] = text.count(word)
        pass
    return my_dict

my_dict = WordsCount(words)

def Freq(text, type, top=10):
    if type == 'most':
        a = sorted(list(text.values()))[-top:]
    elif type == 'least':
        a = sorted(list(text.values()))[:top]
    words = []
    print(a)
    for word, times in text.items():
        if text[word] in a:
            words.append(word)
    return words

            

def MostFreq(text):
    time_used = []
    words = []
    for word, times in text.items():
        while len(time_used) < 10:
            time_used.append(times)
            words.append(word)
        if text[word] > min(time_used):
            for w in words[:]:
                if text[w] == min(time_used):
                    words.remove(w)
            time_used.remove(min(time_used))
            words.append(word)
            time_used.append(times)
    return words

    
        
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

def main():
  # Open the file, read it into memory as a single string.
  with open('alice_in_wonderland.txt') as alice_file:
    alice_text = alice_file.read()
    
  print ('Unique words:', GetUniqueWords(alice_text))
  
  
  
  


if __name__ == '__main__':
  main()
