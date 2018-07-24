import pytest
from candidates import CandidatesAPI
name = 'Marian'
position = 'QA'
class TestCandidatesAPI:
    def test_get_candidate_status_code_list(self):
        assert CandidatesAPI().get_all_candidates().status_code == 200
    def test_get_candidate_json_list(self):
        assert CandidatesAPI().get_all_candidates().json()
    def test_candidate_status_code_get(self):
        new = CandidatesAPI().create_candidate(name, position)
        assert new.status_code == 201  # preconditions
        id = new.json()['candidate']['id']
        assert CandidatesAPI().get_candidate_by_id().status_code == 200