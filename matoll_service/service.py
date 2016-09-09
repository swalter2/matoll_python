# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask, jsonify, request
import sys
from database import *

from nltk.parse import malt
# With MALT_PARSER and MALT_MODEL environment set.
project_path = '/Users/swalter/Git/matoll_python/matoll_service/'
mp = malt.MaltParser(project_path+'resource/maltparser-1.9.0', project_path+'resource/engmalt.linear-1.7.mco')

service = Flask(__name__)



def get_parsed_sentence(plain_sentence):
    depGraph = mp.parse_one(plain_sentence.split())
    Conll = depGraph.to_conll(10)
    return Conll


@service.route('/parsing', methods=['GET'])
def parse_sentences():
    print('in call')
    if request.headers['Content-Type'] == 'application/json':
        try:
            json_input = request.json
            print(json_input)
            plain_sentence = json_input['sentence']
            result = {}
            result['input'] = plain_sentence
            parsed_sentence = get_parsed_sentence(plain_sentence)
            result['output'] = parsed_sentence
            return jsonify(result)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return "500 Server Error ;)"
    else:
        return "415 Unsupported Media Type ;)"


@service.route('/matoll', methods=['GET'])
def ask_for_term():
    if request.headers['Content-Type'] == 'application/json':
        try:
            json_input = request.json
            term = ''
            pos = ''
            uri = ''
            try:
                term = json_input['term']
            except:
                pass

            try:
                uri = json_input['uri']
            except:
                pass

            try:
                pos = json_input['pos']
            except:
                pass
            if term != '':
                return jsonify(get_entries_by_name(term))

            if pos != '':
                return jsonify(get_entries_by_pos(pos))

            if uri != '':
                return jsonify(get_entries_by_uri(uri))

        except:
            print("Unexpected error:", sys.exc_info()[0])
            return "500 Server Error ;)"
    else:
        return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
    service.run(debug=False)
