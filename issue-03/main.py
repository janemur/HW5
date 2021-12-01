from typing import List, Tuple
import unittest


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


class TestTF(unittest.TestCase):
    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_days(self):
        name = ['Monday', 'Tuesday', 'Sunday']
        exp_transformed_name = [
            ('Monday', [0, 0, 1]),
            ('Tuesday', [0, 1, 0]),
            ('Sunday', [1, 0, 0]),
        ]
        x = (fit_transform(name) == exp_transformed_name)
        self.assertTrue(x)

    def test_counties(self):
        subject = ['Russia', 'USA', 'Italy', 'Spain']
        exp_transformed_subject = [
            ('Russia', [0, 0, 0, 1]),
            ('USA', [0, 0, 1, 0]),
            ('Italy', [0, 1, 0, 0]),
            ('Spain', [1, 0, 0, 0])
        ]
        x = (fit_transform(subject) == exp_transformed_subject)
        self.assertTrue(x)

    def test_exception(self):
        with self.assertRaises(TypeError):
            e = fit_transform(0)


if __name__ == '__main__':
    unittest.main()
