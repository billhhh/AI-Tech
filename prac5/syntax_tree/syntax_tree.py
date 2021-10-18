import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP
VP -> V NP | V NP PP
Det -> 'a' | 'The' | 'the'
N -> 'boy' | 'girl' | 'telescope'
V -> 'sees'
P -> 'with'
""")

sent = ['The', 'boy', 'sees', 'the', 'girl', 'with', 'a', 'telescope']
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent):
    print(tree)

parser = nltk.parse.RecursiveDescentParser(grammar)
for tree in parser.parse(sent):
    print(tree)
