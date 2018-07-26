import requests
import json
url = 'http://qainterview.cogniance.com/candidates'
name = 'Marian'
position = 'QA'

class CandidatesAPI:
    def get_all_candidates(self):
        r = requests.get(url)
        return r

    def get_candidate_by_id(self, cid):
        r_id = requests.get(url+r'/'+str(cid))
        return r_id

    def create_candidate(self, name, position):
        data = {'name': name,
                'position': position}
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},
                                      data=json.dumps(data))
        return res_new_cand

    def post_without_headers(self, name, position):
        data = {'name': name,
                'position': position}
        res_new_cand = requests.post(url,

                                     data=json.dumps(data))
        return res_new_cand

    def post_bad_body_with_two_names(self, name, name2, position):
        data = {'name' 'name': name,
                'position': position}
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},

                                     data=json.dumps(data))
        return res_new_cand

    def post_bad_body_without_name(self, position):
        data = {'position': position}
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},

                                     data=json.dumps(data))
        return res_new_cand

    def post_bad_body(self, position, name, id):
        data = {'pos': position,
                'nam': name,
                'id': id,
                }
        res_new_cand = requests.post(url,
                                     headers={'content-type': 'application/json'},

                                     data=json.dumps(data))
        return res_new_cand

    def post_with_bad_url(self, badurl):
        data = {'name': name,
                'position': position}
        res_new_cand = requests.post(badurl,
                                     headers={'content-type': 'application/json'},

                                     data=json.dumps(data))
        return res_new_cand

    def delete_candidate_by_id(self, delid):
        del_id = requests.delete(url+r'/'+str(delid))
        return del_id