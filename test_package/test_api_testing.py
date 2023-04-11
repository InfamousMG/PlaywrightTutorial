import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)

# Verify the response status code
assert response.status_code == 200

# Verify the response contains the expected data
def test_expected():
    expected_data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    assert response.json() == expected_data




