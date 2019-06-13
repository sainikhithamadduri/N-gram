
# coding: utf-8

# In[16]:

# Introduction :


#Authors : Merin Joy and Sai Nikitha
#Date : 4th October 2018
#The following code generates given number of sentences based on the ngram model taking text files as input.


# Instructions to run :


#Step 1: Run the following code in command line.
#Step 2: Give the file name, n, m, text files as ngram.py 3 10 AnnaKarenina1.txt AnnaKarenina2.txt CrimeandPunishment.txt.
#Step 3: The program will then generate sentences using the ngrams, no.of sentences provided.


#Sample Output


#(base) C:\Users\Merin\Desktop\AIT690>python Merin.py 3 10 AnnaKarenina1.txt AnnaKarenina2.txt CrimeandPunishment.txt

#Sentence 1:
#he almost smiled at himself inhis anger ....

#Sentence 2:
#strange to him that there are no barriers and it’ s prison again.marfa petrovna had not uttered a sudden he stood againstthe wall, ticking away hurriedly, with a defiant and offended face.silence lasted for twominutes.

#Sentence 3:
#perhaps, too, and was beingredecorated at his insinuations, hegradually began being in the corner, probably will not refuse this time ....

#Sentence 4:
#of course that’ s album, and i knew your secret.

#Sentence 5:
#he promised to marry her daughter, a neighbour,’ says he.

#Sentence 6:
#well, i am afraid of it, because i canreason that i am very ill, the fact was very heedless ... ” “ but why did they get there.

#Sentence 7:
#she looked at himdifferently ; he attached himself to be a very great deal, if you have, but i might ( with luck ) hope to get round you, ” said raskolnikov who, directly they are really provided for and praises—i hate that good nature, which excited a sarcastic smile in andreysemyonovitch lebeziatnikov, and ... and do you want the money the daybefore.

#Sentence 8:
#iwill put those two stuck-updraggletails ” if they were particularly irksometo him.

#Sentence 9:
#and why on the staircase, he got into the doorway, notknowing what she was a certain and definite ; a firm purpose in hismind.

#Sentence 10:
#he stopped short, kindly examineme or let me know it all.


#Algorithm:

#Step1: Start
#Step2: Combining the input text files and converting them to lower case.
#Step3: Generating sentence and word tokens and adding start, end tags 
#Step4: Generating ngram sentences
    #Step4.1: Calculating frequency and probability
    #Step4.2: Predicting the next word
    #Step4.3: Display the sentences
#Step5: End


#Import systems, regular expressions and nltk
import sys, re, nltk 
#Import util class from nltk library alongwith ngrams
from nltk.util import ngrams
#Import collections library from python alongwith Counter
from collections import Counter
#Import probability class from nltk library alongwith FreqDist and MLEProbDist
from nltk.probability import FreqDist, MLEProbDist

# Initializing system arguments
arg = sys.argv
arg[1] = int(arg[1])
arg[2] = int(arg[2])
#print(arg)

#gen_text function to generate text by Combining the documents and converting them to lower case
def gen_text():
    global arg
    text = b''
    if len(arg) < 4:
        print ("Please give sufficient parameters")
        sys.exit (0)
    for i in range (3,len(arg)):
        f = open(arg[i],"rb")
        text += f.read()
    text = text.decode(encoding='utf-8')
    text = text.lower()
    text = re.sub('\\r\\n','',text.rstrip())
    return text

# gen_tokens function to generate tokens
def gen_tokens(text):
    global arg
    # n in ngrams
    n = arg[1]
    # sentence tokens
    sen_tokens = nltk.tokenize.sent_tokenize(text)
    tokens = []
    
    for i in range(len(sen_tokens)):
        # word tokens
        word_tokens = nltk.tokenize.word_tokenize(sen_tokens[i])
        if (len(word_tokens)  < n):
            # not sufficient characters
            continue
        for i in range (n-1):
            # attaching start and end tags
            word_tokens.append("<END>")
            word_tokens.insert(0, "<START>")
       
        tokens += word_tokens
    # creating ngrams
    ngram = ngrams(tokens,n)
    # counting the number of ngrams
    ngram_count = Counter(ngram)
    # token ngram dictionary
    token_dict = {}
    for index, val in ngram_count.items():
        index2 = index[:-1]
        if index2 in token_dict.keys():
            token_dict[index2][index[-1]] = val
            continue
        token_dict[index2]= {index[-1]: val}
    return token_dict

#gen_sentence to generate sentences
def gen_sentence(ngram):
    global arg
    i = 0
    # n in ngrams
    n = arg[1]
    # number of sentences to generate
    m = arg[2]
    for  i in range (m):
        j = True
        table = []
        sentence = ""
        for size in range (n-1):
            table.append('<START>')
        while j == True:
            tuple_table = tuple(table)
            if tuple_table not in ngram.keys():
                # when start is not available
                sys.exit("No start line!")
            # generating frequency
            frequency = FreqDist(ngram[tuple_table])
            # generating probability
            probability = MLEProbDist(frequency)
            # predicting the next word
            pred_word = probability.generate()
            
            # words having ".,?,!"
            if (pred_word =="." or pred_word == "?" or pred_word == "!"):
                j = False
                sentence += pred_word
                continue
            # words having , ' or START tag
            elif (pred_word == "," or pred_word == "’" or tuple_table[-1] == '<START>'):
                sentence += pred_word
            else:
                sentence += " %s"%pred_word
            table.pop(0)
            table.append(pred_word)
        # Display sentences
        print ("\nSentence %s:\n%s"%(i+1,sentence))

# Main function
def main():
    text = gen_text()
    ngram = gen_tokens(text)
    gen_sentence(ngram)

# Start executing
if __name__ == "__main__":
    main()
    sys.exit(0)


