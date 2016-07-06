#!/usr/bin/python
from rdflib import Graph
import glob
import pprint
import os
path = '/Users/swalter/Downloads/tmp_extractPropertiesWithData/results/ontologySentences_EN/dbpedia/ontology/en/spouse'



for file in os.listdir(path):
    if file.endswith(".ttl"):
        g = Graph()
        print(file)
        g.parse(path+"/"+file, format="turtle")
        print("loaded graph")
        query_1 = "SELECT ?form ?e1_arg ?e2_arg WHERE { ?e1 <conll:head> ?verb . " \
                  "{?e1 <conll:deprel> \"pobj\".} UNION {?e1 <conll:deprel> \"nsubj\".} " \
                  "?verb <conll:cpostag> ?verb_pos. FILTER regex(?verb_pos, \"VB\") . " \
                  "?noun <conll:head> ?verb . ?noun <conll:form> ?form.  " \
                  "{?noun <conll:deprel> \"pobj\".} UNION {?noun <conll:deprel> \"dobj\".} ?e2 <conll:deprel> \"num\". " \
                  " ?e2 <conll:head> ?noun.  ?e1 <own:senseArg> ?e1_arg. ?e2 <own:senseArg> ?e2_arg. }";
        for row in g.query(query_1,DEBUG = True):
            print(row)