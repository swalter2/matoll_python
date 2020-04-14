#import nltk
#parser = nltk.parse.malt.MaltParser(working_dir="resource/maltparser-1.9.0",mco="engmalt.linear-1.8",additional_java_args=['-Xmx1024m'])
#txt = "This is a test sentence"
#graph = parser.raw_parse(txt)
#graph.tree().pprint()
import os
import tempfile
from nltk.parse import malt
# With MALT_PARSER and MALT_MODEL environment set.
mp = malt.MaltParser('/Users/swalter/Git/matoll_python/matoll_service/resource/maltparser-1.9.0', '/Users/swalter/Git/matoll_python/matoll_service/resource/engmalt.linear-1.7.mco')
Question = "Who directed the Matrix ?".split()
depGraph = mp.parse_one(Question)
Conll = depGraph.to_conll(10)
print(Conll)