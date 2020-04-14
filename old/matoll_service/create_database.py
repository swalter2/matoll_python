#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

import_lines = []
path = '/Users/swalter/Dropbox/'
for line in open(path+'joining_test_3_propertynamespace__withpattern_andSentences.tsv','r'):
    line = line.replace('\n','')
    tmp = line.split('\t')
    tmp.append('EN')
    import_lines.append(tmp)


for line in open(path+'joining_test_3_corpus1_withpattern_andSentences.tsv','r'):
    line = line.replace('\n','')
    tmp = line.split('\t')
    tmp.append('EN')
    import_lines.append(tmp)


for line in open(path+'joining_test_3_german_withpattern_andSentences.tsv','r'):
    line = line.replace('\n','')
    tmp = line.split('\t')
    tmp.append('DE')
    import_lines.append(tmp)


for line in open(path+'joining_test_3_spanish_withpattern_andSentences.tsv','r'):
    line = line.replace('\n','')
    tmp = line.split('\t')
    tmp.append('ES')
    import_lines.append(tmp)

print('extracted data')
try:
    con = lite.connect('matoll.db')
    cur = con.cursor()
    query = 'DROP TABLE IF EXISTS Matoll; CREATE TABLE Matoll(Form TEXT, Prep TEXT, Pos TEXT, Frame TEXT , Uri TEXT, Subj TEXT, Obj TEXT, Freq INT, Pattern TEXT, Sentences TEXT, Languages Text);'
    cur.executescript(query)
    con.commit()
    con.executemany('INSERT INTO Matoll VALUES (?,?,?,?,?,?,?,?,?,?,?)', import_lines)
    con.commit()
    query_index = 'CREATE INDEX index_form ON Matoll (Form); ' \
                  'CREATE INDEX index_uri ON Matoll (Uri); ' \
                  'CREATE INDEX index_pattern ON Matoll (Pattern); ' \
                  'CREATE INDEX index_prep ON Matoll (Prep); ' \
                  'CREATE INDEX index_pos ON Matoll (Pos);'
    print('Create Indexes')
    cur.executescript(query_index)

    con.commit()

except:

    if con:
        con.rollback()
    print("Unexpected error:", sys.exc_info()[0])

finally:

    if con:
        con.close()
