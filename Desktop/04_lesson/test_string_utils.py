import pytest
from string_utils import StringUtils


class TestStringUtils:
    # ====================
    # Тесты для capitalize
    # ====================
    @pytest.mark.parametrize("text, expected", [
        ("тест", "Тест"),
        ("123", "123"),
        ("04 апреля 2023", "04 апреля 2023"),
        (" ", " "),
    ])
    def test_capitalize_positive(self, text, expected):
        assert StringUtils.capitalize(text) == expected

    def test_capitalize_negative_empty(self):
        # Ожидаем ошибку, так как код не готов к эксплуатации (красный тест)
        with pytest.raises(IndexError):
            StringUtils.capitalize("")

    def test_capitalize_negative_none(self):
        with pytest.raises(TypeError):
            StringUtils.capitalize(None)

    # ====================
    # Тесты для reverse
    # ====================
    @pytest.mark.parametrize("text, expected", [
        ("тест", "тсет"),
        ("123", "321"),
        ("04 апреля 2023", "3202 ялерпа 40"),
        ("", ""),
    ])
    def test_reverse_positive(self, text, expected):
        assert StringUtils.reverse(text) == expected

    def test_reverse_negative_none(self):
        with pytest.raises(TypeError):
            StringUtils.reverse(None)

    # ====================
    # Тесты для is_palindrome
    # ====================
    @pytest.mark.parametrize("text, expected", [
        ("А роза упала на лапу Азора", True),
        ("12321", True),
        ("Тест", False),
        ("", True),  # Пустая строка технически является палиндромом
    ])
    def test_is_palindrome_positive(self, text, expected):
        assert StringUtils.is_palindrome(text) is expected

    def test_is_palindrome_negative_none(self):
        with pytest.raises(AttributeError):
            StringUtils.is_palindrome(None)

    # ====================
    # Тесты для count_words
    # ====================
    @pytest.mark.parametrize("text, expected", [
        ("Привет мир", 2),
        ("123 456", 2),
    ])
    def test_count_words_positive(self, text, expected):
        assert StringUtils.count_words(text) == expected

    def test_count_words_negative_spaces(self):
        # Проверка корректного поведения: строка из пробелов должна содержать 0 слов.
        # Этот тест упадет (будет красным), что подтверждает наличие дефекта в коде!
        assert StringUtils.count_words("  ") == 0

    def test_count_words_negative_none(self):
        with pytest.raises(AttributeError):
            StringUtils.count_words(None)