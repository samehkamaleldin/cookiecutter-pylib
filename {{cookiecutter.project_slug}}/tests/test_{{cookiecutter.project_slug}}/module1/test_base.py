from {{cookiecutter.project_slug}}.module1 import AClass


def test_a_class():
    a = AClass(name="test")
    assert a.name == "test"
