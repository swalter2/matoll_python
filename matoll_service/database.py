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
            tmp['Form'] = tmp[0]
            tmp['Prep'] = tmp[1]
            tmp['Uri'] = tmp[2]
            tmp['Freq'] = tmp[3]
            tmp['Pos'] = tmp[4]
            tmp['Frame'] = tmp[5]
            tmp['Pattern'] = tmp[6]
            tmp['Subj'] = tmp[7]
            tmp['Obj'] = tmp[8]
            result[tmp[0]+'_'+str(counter)] = tmp
    con.close()
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
            tmp['Form'] = tmp[0]
            tmp['Prep'] = tmp[1]
            tmp['Uri'] = tmp[2]
            tmp['Freq'] = tmp[3]
            tmp['Pos'] = tmp[4]
            tmp['Frame'] = tmp[5]
            tmp['Pattern'] = tmp[6]
            tmp['Subj'] = tmp[7]
            tmp['Obj'] = tmp[8]
            result[tmp[0] + '_' + str(counter)] = tmp
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
            tmp['Form'] = tmp[0]
            tmp['Prep'] = tmp[1]
            tmp['Uri'] = tmp[2]
            tmp['Freq'] = tmp[3]
            tmp['Pos'] = tmp[4]
            tmp['Frame'] = tmp[5]
            tmp['Pattern'] = tmp[6]
            tmp['Subj'] = tmp[7]
            tmp['Obj'] = tmp[8]
            result[tmp[0] + '_' + str(counter)] = tmp
    con.close()
    return result