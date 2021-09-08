import nltk
from nltk.tokenize import TweetTokenizer
class Case:
    def __init__(self):
        pass

    def sentenceCase(self, text):
        tt = text

        word1 = nltk.word_tokenize(tt.lower())
        word_pos = nltk.pos_tag(word1)
        print(word_pos)
        all_text = []
        for a, b in word_pos:
            if b == "NNP" or b == "NN" or b=='PRP':
                all_text.append(a.capitalize())
            else:
                all_text.append(a)
        print("sentence")
        return all_text


    def titleCase(self, text):
        tknzr = TweetTokenizer()
        word1 = tknzr.tokenize(text)
        #word1 = text.split(" ")
        print(word1)

        word_pos = nltk.pos_tag(word1)
        #print(word_pos)
        all_texts = []
        for a, b in word_pos:
            if(b=="DT" or b =="TO" or b=="IN" or b=="CC" or b=="RB" or b=="VBP"):
                all_texts.append(a)
            elif(b=="NN" or b=="NNP" or b=="NNS"):
                if a.isupper():
                    all_texts.append(a)
                else:
                    all_texts.append(a.capitalize())
            else:
                all_texts.append(a.capitalize())
        #print("--title--*25")
        return all_texts