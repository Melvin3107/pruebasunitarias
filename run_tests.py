import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_addition():
    response = requests.get(f'{BASE_URL}/add', params={'a': 1, 'b': 2})
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_subtraction():
    response = requests.get(f'{BASE_URL}/subtract', params={'a': 5, 'b': 3})
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_multiplication():
    response = requests.get(f'{BASE_URL}/multiply', params={'a': 2, 'b': 4})
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_division():
    response = requests.get(f'{BASE_URL}/divide', params={'a': 8, 'b': 2})
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

def test_division_by_zero():
    response = requests.get(f'{BASE_URL}/divide', params={'a': 8, 'b': 0})
    assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_division_by_zero()
    print("All tests passed.")
