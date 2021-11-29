from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_days():
    days = ['Monday', 'Tuesday', 'Sunday']
    exp_transformed_days = [
        ('Monday', [0, 0, 1]),
        ('Tuesday', [0, 1, 0]),
        ('Sunday', [1, 0, 0]),
    ]
    assert fit_transform(days) == exp_transformed_days


def test_counties():
    countries = ['Russia', 'USA', 'Italy', 'Spain']
    exp_transformed_cointries = [
        ('Russia', [0, 0, 0, 1]),
        ('USA', [0, 0, 1, 0]),
        ('Italy', [0, 1, 0, 0]),
        ('Spain', [1, 0, 0, 0])
    ]
    assert fit_transform(countries) == exp_transformed_cointries


def test_exception():
    with pytest.raises(TypeError):
        e = fit_transform(0)


