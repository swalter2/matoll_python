#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def get_entries_by_name(name):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj FROM Matoll where Form=:form;",{"form": name})
        rows = cur.fetchall()
        counter = 0
        for row in rows:
            tmp = {}
            counter+=1
            tmp['Form'] = row[0]
            tmp['Prep'] = row[1]
            tmp['Uri'] = row[2]
            tmp['Freq'] = row[3]
            tmp['Pos'] = row[4]
            tmp['Frame'] = row[5]
            tmp['Pattern'] = row[6]
            tmp['Subj'] = row[7]
            tmp['Obj'] = row[8]
            result[row[0]+'_'+str(counter)] = tmp
    con.close()
    print(result)
    return result


def get_entries_by_pos(pos):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj FROM Matoll where Pos=:pos;",{"pos": pos})
        rows = cur.fetchall()
        counter = 0
        for row in rows:
            tmp = {}
            counter += 1
            tmp['Form'] = row[0]
            tmp['Prep'] = row[1]
            tmp['Uri'] = row[2]
            tmp['Freq'] = row[3]
            tmp['Pos'] = row[4]
            tmp['Frame'] = row[5]
            tmp['Pattern'] = row[6]
            tmp['Subj'] = row[7]
            tmp['Obj'] = row[8]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result


def get_entries_by_uri(uri):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj FROM Matoll where Uri=:uri;",{"uri": uri})
        rows = cur.fetchall()
        counter = 0
        for row in rows:
            tmp = {}
            counter += 1
            tmp['Form'] = row[0]
            tmp['Prep'] = row[1]
            tmp['Uri'] = row[2]
            tmp['Freq'] = row[3]
            tmp['Pos'] = row[4]
            tmp['Frame'] = row[5]
            tmp['Pattern'] = row[6]
            tmp['Subj'] = row[7]
            tmp['Obj'] = row[8]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result


def get_entries_by_frequency(freq):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj FROM Matoll where Freq>=:freq;",{"freq": freq})
        rows = cur.fetchall()
        counter = 0
        for row in rows:
            tmp = {}
            counter += 1
            tmp['Form'] = row[0]
            tmp['Prep'] = row[1]
            tmp['Uri'] = row[2]
            tmp['Freq'] = row[3]
            tmp['Pos'] = row[4]
            tmp['Frame'] = row[5]
            tmp['Pattern'] = row[6]
            tmp['Subj'] = row[7]
            tmp['Obj'] = row[8]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result
