import requests
import json
url = 'http://qainterview.cogniance.com/candidates'
id = '13'

class CandidatesAPI:
    def get_all_candidates(self):
        r = requests.get(url)
        return r

    def get_candidate_by_id(self):
        r_id = requests.get(url+r'/'+id)

    def create_candidate(self, name, position):
        data = {'name': name,
                'position': position}
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},
                                      data=json.dumps(data))

    def delete_candidate_by_id(self):
        del_id = requests.delete(url+id)