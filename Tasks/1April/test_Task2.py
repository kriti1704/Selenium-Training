""" TASK 2: Pytest Markers Practice

Create 2 custom markers:
@pytest.mark.smoke
@pytest.mark.regression
Write:
2 test cases for smoke
2 test cases for regression
Each test should:
Contain a simple assertion 
Run tests using:
Only smoke tests
Only regression tests """
import pytest

# pytest.mark.smoke
@pytest.mark.smoke
def test_login():
    assert "admin" == "admin", "Can't Login"

@pytest.mark.smoke
def test_homepage_title():
    assert "Home" in "Home Page", "Not in home page"

# pytest.mark.regression
@pytest.mark.regression
def test_membership():
    l = ['apple','banana','cherry']
    assert 'cherry' in l, "Cherry not in list"

@pytest.mark.regression
def test_not_membership():
    l = ['apple','banana','cherry']
    assert 'kiwi' not in l, "Kiwi in list"

# run smoke tests
# pytest -vs test_Task2.py -m "smoke"

# run regression tests
# pytest -vs test_Task2.py -m "regression"