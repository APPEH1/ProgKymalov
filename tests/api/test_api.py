"""
def test_check_math():
    assert 7*7 == 49

def test_check_math():
    assert 7*8 == 56"""

import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Valentyn'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Kymalov'
