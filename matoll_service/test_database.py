#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('matoll.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT DISTINCT  Form, Prep, Freq, Pos, Frame, Pattern, Subj, Obj FROM Matoll where Form=:form;",{"form": 'wife'})

    rows = cur.fetchall()

    for row in rows:
        print(row)
con.close()