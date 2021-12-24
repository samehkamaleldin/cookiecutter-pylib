from {{cookiecutter.project_slug}}.module2 import sum_nums, product_nums


def test_sum_nums():
    assert sum_nums([1, 2]) == 3
    assert sum_nums([1, 2, 3]) == 6
    assert sum_nums([1, 2, 3, 4]) == 10


def test_product_nums():
    assert product_nums([1, 2]) == 2
    assert product_nums([1, 2, 3]) == 6
    assert product_nums([1, 2, 3, 4]) == 24
