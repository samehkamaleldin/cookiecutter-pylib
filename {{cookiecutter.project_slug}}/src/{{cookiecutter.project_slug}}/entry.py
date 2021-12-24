import {{cookiecutter.project_slug}}


def main():
    """Return the main entry point for the program."""
    version = {{cookiecutter.project_slug}}.__version__
    print(f"Hello World! from pylib version: {version}")


if __name__ == "__main__":
    main()
