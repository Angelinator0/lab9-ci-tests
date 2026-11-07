import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Создаёт новый экземпляр Calculator для каждого теста."""
    return Calculator()


# ---------- Тесты метода add ----------

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),                  # два положительных
    (-2, -3, -5),               # два отрицательных
    (-5, 5, 0),                 # противоположные числа
    (0, 0, 0),                  # нули
    (0, 7, 7),                  # ноль и число
    (1.5, 2.5, 4.0),            # дробные числа
    (1000000, 2000000, 3000000) # большие числа
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


def test_add_float_precision(calc):
    # 0.1 + 0.2 в float не равно ровно 0.3, поэтому сравниваем с допуском
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


# ---------- Тесты метода divide ----------

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),                 # деление нацело
    (10, 4, 2.5),               # дробный результат
    (-10, 2, -5),               # отрицательное делимое
    (10, -2, -5),               # отрицательный делитель
    (-10, -2, 5),               # оба отрицательные
    (0, 5, 0),                  # ноль в делимом
    (1, 3, 1 / 3),              # периодическая дробь
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
    (3.5, 0),
    (5, 0.0),
])
def test_divide_by_zero_raises(calc, a, b):
    # Тест проходит, только если выброшено исключение ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        calc.divide(a, b)


def test_divide_by_zero_message(calc):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
        calc.divide(1, 0)


# ---------- Тесты метода is_prime_number ----------

@pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 97, 7919])
def test_is_prime_true(calc, n):
    # 2 — единственное чётное простое, 7919 — большое простое
    assert calc.is_prime_number(n) is True


@pytest.mark.parametrize("n", [4, 6, 9, 15, 25, 49, 100, 7917])
def test_is_prime_false_for_composite(calc, n):
    # 9, 25, 49 — квадраты простых: проверяют границу цикла i * i <= n
    assert calc.is_prime_number(n) is False


@pytest.mark.parametrize("n", [1, 0, -1, -7, -100])
def test_is_prime_false_below_two(calc, n):
    # простыми считаются только числа от 2
    assert calc.is_prime_number(n) is False


@pytest.mark.parametrize("value", [7.5, "7", None, 7.0])
def test_is_prime_invalid_type_raises(calc, value):
    # не целые значения должны вызывать TypeError
    with pytest.raises(TypeError):
        calc.is_prime_number(value)
