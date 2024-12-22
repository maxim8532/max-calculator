import pytest
from calculator import Calculator


@pytest.mark.parametrize("expression", [
    # Up to 5 simple syntax errors
    "2*^3",
    "1??2",
    "3..4",
    "((((((",
    "2^*3"
])
def test_syntax_errors(expression):
    calc = Calculator(expression)
    result = calc.calculate()
    #  The code raises exceptions instead of
    assert result is None, (
        f"Expected an invalid result (None) for syntax error '{expression}', "
        f"but got {result}"
    )


def test_gibberish():
    calc = Calculator("blablabla")
    result = calc.calculate()
    assert result is None, (
        "Expected an invalid result (None) for gibberish, but got "
        f"{result}"
    )


def test_empty_string():
    calc = Calculator("")
    result = calc.calculate()
    assert result is None, (
        "Expected an invalid result (None) for empty string, but got "
        f"{result}"
    )


def test_whitespace_string():
    calc = Calculator("   \t   ")
    result = calc.calculate()
    assert result is None, (
        "Expected an invalid result (None) for whitespace-only string, but got "
        f"{result}"
    )


simple_expressions = [
    ("1+2", 3),
    ("5-3", 2),
    ("2*3", 6),
    ("10/2", 5),
    ("2^3", 8),
    ("-5", -5),
    ("11%3", 2),
    ("1$2", 2),
    ("2&3", 2),
    ("2@4", 3),
    ("3!", 6),
    ("~5", -5),
    ("-(~3)", 3),
    ("(2+3)*4", 20),
    ("123#", 6)
]


@pytest.mark.parametrize("expression, expected", simple_expressions)
def test_simple_expressions(expression, expected):
    calc = Calculator(expression)
    result = calc.calculate()
    assert result is not None, (
        f"Expected a valid number for '{expression}', but got None (invalid)."
    )
    assert result == expected, (
        f"Expected {expected} but got {result} for '{expression}'"
    )


complex_expressions = [
    ("((2 + 3 * 4 ) - (5 % 2 ))", 13),
    (" (10 @ 20 )  + (3 ^ 2 ) / (2 & 4) ", 19.5),
    ("( 5 + ( 8 - ( 6# ) ) * 2 )", 9),
    ("((12 #) * (3!)) ^ (4) ", 104976),
    ("(7$3) ^ 2 - (10%3) + (6&5 * 2) ", 58),
    ("(10$2) & (20@4) + -((4#)/(3%2))", 14),
    ("((2+3*4)/(5-2))^(2$1)", 21.7777777778),
    ("( ( 3 * ( 2+5 ) ) - ( ~4 ) ) ^ (3!)", 244140625),
    ("((10 * 2) - 3!) % ( ~5 + 10 )", 4),
    ("12! / ((10@2) ^ (3&5))", 2217600),
    (" ( ( (8&4) + (9$3) ) ^ ( 3! ) ) - ( 2@4 ) ", 4826806),
    ("(10#)^((1.2+3.4)*2)", 1),
    ("((5 + 5 +5+5+5) * (2@10)) / ( (3$1) - (1%1) )", 50),
    ("((((8#)*2)+((10%3)^(2)))^( (6$3) )) - ~10", 24137579),
    ("(7!) + (8!) + (9!)", 408240),
    (" ((100 @ 50 ) + ( 70 & 30 )) ^ ( 2! ) ", 11025),
    (" ( ( 2! )^( 3! ) ) + ( ( 4! )^( 1%1 ) )", 65),
    (" ( ( (10! ) / (5! ) ) ^ (2.5 ) )", 159020995200.19443),
    (" ((8#) + (9#)) * ((999#)/(100#))", 459),
    ("( ( 3^2 ) + ( (4!) - (5!) ) ) ^ 2", 7569)
]


@pytest.mark.parametrize("expression, expected", complex_expressions)
def test_complex_expressions(expression, expected):
    calc = Calculator(expression)
    result = calc.calculate()
    # Make sure we got a result, not None
    assert result is not None, (
        f"Expected a valid number for '{expression}', but got None."
    )

    # Convert the result to float in case it's large or decimal
    result_float = float(result)

    # If expected is float, allow some tolerance
    if isinstance(expected, float):
        assert abs(result_float - expected) < 1e-5 or \
               (abs(expected) > 1 and abs(result_float - expected) / abs(expected) < 1e-5), \
            f"Expected ~{expected}, got {result_float} for '{expression}'"
    else:
        # If it's an integer scenario, just compare exactly
        assert result == expected, (
            f"Expected {expected}, got {result} for '{expression}'"
        )

@pytest.mark.parametrize("expression, expected", complex_expressions)
def test_complex_expressions(expression, expected):
    result = Calculator(expression).calculate()
    # Must get a non-None result for valid expressions:
    assert result is not None, (
        f"Expected a number for '{expression}', but got None."
    )
    result_float = float(result)
    if isinstance(expected, float):
        # Ease tolerance for large floats
        rel_tol = 1e-5
        abs_diff = abs(result_float - expected)
        rel_diff = abs_diff / abs(expected) if abs(expected) > 1e-12 else abs_diff
        assert (abs_diff < 1e-4) or (rel_diff < rel_tol), (
            f"Expected ~{expected}, got {result_float} for '{expression}'"
        )
    else:
        assert result == expected, (
            f"Expected {expected}, got {result} for '{expression}'"
        )
