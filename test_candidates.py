import pytest
from candidates import ClassCandidatesAPI
class TestsGetList:
    def test_get_candidate_status_code_list(self):
        assert ClassCandidatesAPI().get_all_candidates().status_code == 200
    def test_get_candidate_status_code_list(self):
        assert ClassCandidatesAPI().get_all_candidates().json()
