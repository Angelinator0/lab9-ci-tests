class Calculator:
    """Класс с бизнес-логикой калькулятора."""

    def add(self, a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    def divide(self, a, b):
        """Возвращает результат деления a на b.

        Вызывает ZeroDivisionError, если b равно нулю.
        """
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, n):
        """Проверяет, является ли целое число n простым.

        Вызывает TypeError, если n не целое число.
        """
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым")
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
