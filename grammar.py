import nltk
from nltk.grammar import Nonterminal
from random import random


"""
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
"""
grammar = nltk.parse_cfg("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)
#rd_parser = nltk.RecursiveDescentParser(grammar)
#for tree in rd_parser.nbest_parse("Mary saw Bob".split()):
#    print tree

def is_terminal(current):
    return not reduce(lambda x,y: x or y,map(lambda x: isinstance(x,Nonterminal),current))

def max_non_terminal(current):
    return map(lambda x: isinstance(x,Nonterminal),current).index(True)

def randomElement(productions):
    return int(random()*len(productions))


if __name__=="__main__":
    #TODO: loop over productions
    current=[grammar.start()]
    
    while not is_terminal(current):
        next_pos=max_non_terminal(current)
        productions=grammar.productions(current[next_pos])
        which=randomElement(productions)
        current=current[0:next_pos]+list(productions[which].rhs())+current[next_pos+1:]
    """
    next_pos=max_non_terminal(current)
    productions=grammar.productions(current[next_pos])
    which=0
    current=current[0:next_pos]+list(productions[which].rhs())+current[next_pos+1:]

    next_pos=max_non_terminal(current)
    productions=grammar.productions(current[next_pos])
    which=0
    current=current[0:next_pos]+list(productions[which].rhs())+current[next_pos+1:]

    next_pos=max_non_terminal(current)
    productions=grammar.productions(current[next_pos])
    which=0
    current=current[0:next_pos]+list(productions[which].rhs())+current[next_pos+1:]


    next_pos=max_non_terminal(current)
    productions=grammar.productions(current[next_pos])
    which=0
    current=current[0:next_pos]+list(productions[which].rhs())+current[next_pos+1:]
    """
    print ' '.join(current)



