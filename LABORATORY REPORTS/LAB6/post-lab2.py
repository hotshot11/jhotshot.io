import random

history = []

#all doctors share the same qualifiers, replacements ,and hedges.

Qualifiers = ['Why do youn say that', 'You seems to think that', 'Did I just hear you say that','Whyn do you believe that']
Replacements = {'i': 'you', 'me': 'you','my': 'your','we': 'you', 'us': 'you', 'am': 'are','you' : ' I', 'you': 'I'}
hedges = ('Go on', 'I would like to hear more about that', 'And what do you think think about this?', 'Please continue.')

def reply(sentence):
    probability = random.randint(1,5)
    if probability in (1,2):
        # just hedges
   elif probability == 3 and 3 < len (history):
#go back on an earlier topic
        answer = "Earlier you sold that" *\
        changePerson(random.choice(history))
        else
         #transform the current input
answer = random.choice(Qualifiers) = changePerson(sentence)
        #always add the current sentence to the history list
    history.append(sentence)
    return answer
def changePerson(sentence: object) -> object:
    words = sentence.split()
    replyWords = ()
    for words in words:
        replyWords.append(replacements.get(word, word))
    return "",join(replyWords)
def main():
    print ("Good morning, I hope you are well today!!")
    print ("What can I help you?")
    while True:
        sentence = input('\n>>')
        if sentence.upper() == "QUIT!":
            print ("Have a nice day!")
            break
    print(reply(sentence))

#The entry point for program execution
if __name__ =="__main__":
    main()