#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def get_entries_by_name(name, lang = 'EN'):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj, Languages FROM Matoll "
                    "where Form=:form and Languages=:lang;",{"form": name, 'lang':lang})
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
            tmp['Languages'] = row[9]
            result[row[0]+'_'+str(counter)] = tmp
    con.close()
    return result


def get_entries_by_pos(pos, lang = 'EN'):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj, Languages FROM Matoll "
                    "where Pos=:pos and Languages=:lang;",{"pos": pos, 'lang':lang})
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
            tmp['Languages'] = row[9]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result


def get_entries_by_uri(uri, lang = 'EN'):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj, Languages FROM Matoll "
                    "where Uri=:uri and Languages=:lang;",{"uri": uri, 'lang':lang})
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
            tmp['Languages'] = row[9]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result

def get_entries_by_frequency(freq, lang = 'EN'):
    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj, Languages FROM Matoll "
                    "where Freq>=:freq and Languages=:lang;",{"freq": freq, 'lang':lang})
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
            tmp['Languages'] = row[9]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result


def get_combined_result (freq, uri, pos, name, lang = 'EN'):

    con = lite.connect('matoll.db')
    result = {}
    with con:
        cur = con.cursor()
        query = "SELECT DISTINCT  Form, Prep, Uri, Freq, Pos, Frame, Pattern, Subj, Obj, Languages FROM Matoll where "

        hm = {}
        if freq != '':
            query += "Freq>=:freq and "
            hm['freq'] = freq

        if uri != '':
            query += "Uri=:uri and "
            hm['uri'] = uri

        if pos != '':
            query += "Pos=:pos and "
            hm['pos'] = pos

        if name != '':
            query += "Form=:form and "
            hm['form'] = name

        if lang != '' and lang != 'NONE':
            query += "Languages=:lang and "
            hm['lang'] = lang

        if query.endswith("and "):
            query = query[:-4]

        query+=';'

        cur.execute(query,hm)
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
            tmp['Languages'] = row[9]
            result[row[0] + '_' + str(counter)] = tmp
    con.close()
    return result