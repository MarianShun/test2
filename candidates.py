import requests
import json
url = 'http://qainterview.cogniance.com/candidates'
name = 'Marian'
position = 'QA'
id = '13'
def test_answer():
    assert 2 + 2 == 4
	
def test_answer1():
    assert 1 + 1 == 2
	
def test_answer2():
    assert 2 + 1 == 3

word1 = 'hello'
space = ' '
word2 = 'world'

def test_hello_world():
    assert word1 + space + word2 == 'hello world'
    print('hello, world')

class ClassCandidatesAPI:
    def get_all_candidates(self):
        r = requests.get(url)
        return r

    def get_candidate_with_id(self):
        r_id = requests.get(url+id)

    def create_candidate(self, name, position):
        data = {'name': name,
                'position': position}
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},
                                      data=json.dumps(data))

    def delete_candidate_with_id(self):
        del_id = requests.delete(url+id)