import pytest
import json
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
   
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    
    r = github_api.get_user('kymalovvalentyn')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 55
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('kymalovvalentyn_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

#індивідуальна робота:
    
@pytest.mark.api
def test_get_emojis():
    github_api = GitHub()
    emojis = github_api.get_emojis()
    print(emojis)
    assert isinstance(emojis, dict)
    assert 'fire' in emojis.keys()
    
@pytest.mark.api
def test_get_emojis_not_empty():
    github_api = GitHub()
    emojis = github_api.get_emojis()
    assert isinstance(emojis, dict)
    assert len(emojis) > 0
 
@pytest.mark.api
def test_get_commits():
    github_api = GitHub()
    owner = 'APPEH1' 
    repo = 'PROGKYMALOV'    
    commits = github_api.get_commits(owner, repo)
    assert isinstance(commits, list)
    assert len(commits) > 0
    print(f"Кількість комітів: {len(commits)}")