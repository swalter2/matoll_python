#!/usr/bin/python

from flask import json, Flask, request, jsonify
app = Flask(__name__)
results_automatic = []
uris_automatic = set()


def load_lexicon(file, frequency=1):
    results = []
    uris = set()
    for line in open(file, 'r'):
        line = line.replace('\n', '')
        tmp = line.split('\t')
        lemma = tmp[0]
        prep = tmp[1]
        pos = tmp[2]
        frame = tmp[3]
        uri = tmp[4]
        subj = tmp[5]
        obj = tmp[6]
        if 'http://dbpedia/' in uri:
            uri = uri.replace('http://dbpedia/','http://dbpedia.org/')
            #TODO: Fix this in the exporter
        entry_frequency = int(tmp[7])
        if entry_frequency >= frequency:
            uris.add(uri)
            results.append([lemma,prep,pos,uri,entry_frequency,frame,subj,obj])
    return results, uris

def get_map(e):
    tmp_hm = {}
    tmp_hm['label'] = e[0]
    tmp_hm['prep'] = e[1]
    tmp_hm['pos'] = e[2]
    tmp_hm['uri'] = e[3]
    tmp_hm['entry_frequency'] = e[4]
    tmp_hm['frame'] = e[5]
    tmp_hm['subj'] = e[6]
    tmp_hm['obj'] = e[7]
    return tmp_hm

def find_entries(label,uri,pos):
    results = {}
    counter = 0
    if label!='' and uri!='' and pos!='':
        for e in results_automatic:
            if e[0] == label and e[3]== uri and e[2] == pos:
                results[counter] = get_map(e)
                counter += 1
    elif label == '' and uri != '' and pos != '':
        for e in results_automatic:
            if e[3] == uri and e[2] == pos:
                results[counter] = get_map(e)
                counter += 1
    elif label == '' and uri == '' and pos != '':
        for e in results_automatic:
            if e[2] == pos:
                results[counter] = get_map(e)
                counter += 1
    elif label == '' and uri != '' and pos == '':
        for e in results_automatic:
            if e[3] == uri:
                results[counter] = get_map(e)
                counter += 1
    else:
        for e in results_automatic:
            if e[0] == label or e[3] == uri or e[2] == pos:
                results[counter] = get_map(e)
                counter += 1
    return results

#GET always one argument
@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

#curl -H "Content-type: application/json" \-X GET http://127.0.0.1:5000/matoll -d '{"message":"Hello Data"}' => Maybe POST is better
@app.route('/matoll', methods = ['GET'])
def api_message():
    if request.headers['Content-Type'] == 'application/json':
        json_input = request.json
        label = ''
        uri = ''
        pos = ''
        if 'label' in json_input:
            label = json_input['label']
        if 'uri' in json_input:
            uri = json_input['uri']
        if 'pos' in json_input:
            pos = json_input['pos']
        return json.dumps(find_entries(label,uri,pos))
    else:
        return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
    results_automatic, uris_automatic = load_lexicon('/Users/swalter/Git/matoll/matoll/test_output_simple.tsv')
    app.run()
