import requests

API_URL = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "category": 15,       # Entertainment: Video Games
    "difficulty": "medium",
    "type": "boolean"
}


def fetch_question_data() -> list[dict]:
    response = requests.get(API_URL, params=PARAMETERS)
    response.raise_for_status()

    data = response.json()

    if data.get("response_code") != 0:
        raise ValueError("Failed to fetch valid questions from the API.")

    return data["results"]


question_data = fetch_question_data()
