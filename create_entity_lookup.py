import codecs

from gensim.models import Word2Vec

f_input = codecs.open("wiki_corpus.txt","r","utf-8")
sent = set()
for line in f_input:
    line = line.replace("\n", "")
    sent.add(line.lower())
print(len(sent))


model = Word2Vec(sent, min_count=1,size= 50,workers=3, window =3, sg = 1)
print(model['europe,'])