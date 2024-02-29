#індивідуальна робота:

"""В цьому коді реалізовано 3 тести 
(2 для методи Emojis та 1 для методу Commits):
Тест 1: отримує Емодзі з GitHub, після чого йде перевірка, чи
        є результат словником, а потім пошук певного Емодзі.
Тест 2: отримує Емодзі з GitHub, після чого перевірка, чи є
        результат словником та чи не порожній він.
Тест 3: викликає метод для отримання списку комітів згідно зазначеного
        репозиторія та його власника. А також перевіряє, щоб
        коміти були наявні та вказує кількість комітів"""

import pytest
from modules.api.clients.github import GitHub
    
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