import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # секунд: не ждать ответ бесконечно


# ---------- GET /users/1 ----------

@pytest.fixture(scope="module")
def get_response():
    """Один запрос GET на все тесты этого блока."""
    return requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)


def test_get_user_status_code_is_200(get_response):
    assert get_response.status_code == 200


def test_get_user_json_structure(get_response):
    user = get_response.json()
    expected_types = {
        "id": int,
        "name": str,
        "username": str,
        "email": str,
        "address": dict,
        "company": dict,
    }
    for field, expected_type in expected_types.items():
        assert field in user, f"В ответе нет поля {field}"
        assert isinstance(user[field], expected_type), (
            f"Поле {field} должно быть типа {expected_type.__name__}"
        )
    assert isinstance(user["address"].get("city"), str)


def test_get_user_field_values(get_response):
    user = get_response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert user["username"] == "Bret"
    assert "@" in user["email"]


# ---------- POST /users ----------

NEW_USER = {
    "name": "Ivan Petrov",
    "username": "ivanp",
    "email": "ivan.petrov@example.com",
}


@pytest.fixture(scope="module")
def post_response():
    """Один запрос POST на все тесты этого блока."""
    return requests.post(f"{BASE_URL}/users", json=NEW_USER, timeout=TIMEOUT)


def test_post_user_status_code_is_201(post_response):
    assert post_response.status_code == 201


def test_post_user_json_structure(post_response):
    created = post_response.json()
    for field, expected_type in {"id": int, "name": str, "username": str, "email": str}.items():
        assert field in created, f"В ответе нет поля {field}"
        assert isinstance(created[field], expected_type), (
            f"Поле {field} должно быть типа {expected_type.__name__}"
        )


def test_post_user_values_match_sent_and_id_assigned(post_response):
    created = post_response.json()
    assert created["name"] == NEW_USER["name"]
    assert created["username"] == NEW_USER["username"]
    assert created["email"] == NEW_USER["email"]
    assert created["id"] > 10


# ---------- PUT /users/1 ----------

UPDATED_USER = {
    "id": 1,
    "name": "Ivan Petrov",
    "username": "ivanp",
    "email": "ivan.petrov@example.com",
}


@pytest.fixture(scope="module")
def put_response():
    """Один запрос PUT на все тесты этого блока."""
    return requests.put(f"{BASE_URL}/users/1", json=UPDATED_USER, timeout=TIMEOUT)


def test_put_user_status_code_is_200(put_response):
    assert put_response.status_code == 200


def test_put_user_json_structure(put_response):
    updated = put_response.json()
    for field, expected_type in {"id": int, "name": str, "username": str, "email": str}.items():
        assert field in updated, f"В ответе нет поля {field}"
        assert isinstance(updated[field], expected_type), (
            f"Поле {field} должно быть типа {expected_type.__name__}"
        )


def test_put_user_id_and_values_match_sent(put_response):
    updated = put_response.json()
    assert updated["id"] == 1
    assert updated["name"] == UPDATED_USER["name"]
    assert updated["username"] == UPDATED_USER["username"]
    assert updated["email"] == UPDATED_USER["email"]
