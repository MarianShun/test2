import pytest
from candidates import CandidatesAPI
name = 'Marian'
position = 'QA'
negative_id = '9b'

class TestCandidatesAPI:
    def test_get_candidate_status_code_list(self):
        assert CandidatesAPI().get_all_candidates().status_code == 200

    def test_candidate_status_code_get(self):
        new = CandidatesAPI().create_candidate(name, position)
        assert new.status_code == 201  # preconditions
        id = new.json()['candidate']['id']
        assert CandidatesAPI().get_candidate_by_id(id).status_code == 200

    neg_ids = ['9b', ';', '\'', '"', '`', ':', '/', '|', '{', ']', '!', '^', '&', '*', '_', '+', '#', '@', ')', '₴',
               '?', '$', '0']
    @pytest.mark.parametrize(('negative_id'), neg_ids)
    def test_candidate_status_code_get_negative_id(self, negative_id):
        assert CandidatesAPI().get_candidate_by_id(str(id) + 'a').status_code == 404

    def test_candidate_status_code_post(self):
        new = CandidatesAPI().create_candidate(name, position)
        assert new.status_code == 201

    def test_candidate_code_post_without_headers(self):
        new = CandidatesAPI().post_without_headers('Marian Shun', 'QA Intern')
        assert new.status_code == 400

    def test_candidate_code_post_body_with_two_names(self):
        new = CandidatesAPI().post_bad_body_with_two_names('Marian Shun', 'Marian Shun', 'QA Intern')
        assert new.status_code == 400

    def test_candidate_code_post_body_without_name(self):
        new = CandidatesAPI().post_bad_body_without_name('QA Intern')
        assert new.status_code == 400

    def test_candidate_code_post_bad_body(self):
        new = CandidatesAPI().post_bad_body('QA Intern', 'Marian Shun', '2018')
        assert new.status_code == 400

    def test_candidate_code_post_with_bad_url(self):
        new = CandidatesAPI().post_with_bad_url('http://qainterview.cogniance.com/candidatez')
        assert new.status_code == 405

    def test_candidate_code_post_del(self):
        new = CandidatesAPI().create_candidate(name, position)
        assert new.status_code == 201  # preconditions
        id = new.json()['candidate']['id']
        assert CandidatesAPI().delete_candidate_by_id(id).status_code == 200

    neg_ids = ['9b', ';', '\'', '"', '`', ':', '/', '|', '{', ']', '!', '^', '&', '*', '_', '+', '#', '@', ')', '₴',
               '?', '$', '0']
    @pytest.mark.parametrize(('negative_id'), neg_ids)
    def test_candidate_status_code_del_negative_id(self, negative_id):
        assert CandidatesAPI().delete_candidate_by_id(negative_id).status_code == 404