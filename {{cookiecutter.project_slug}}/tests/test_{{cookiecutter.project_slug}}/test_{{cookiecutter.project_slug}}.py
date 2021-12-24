import {{cookiecutter.project_slug}}


def test_{{cookiecutter.project_slug}}():
    ver = {{cookiecutter.project_slug}}.__version__
    assert len(ver) > 3
