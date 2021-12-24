import {{cookiecutter.project_slug}}


def main():
    """Return the main entry point for the program."""
    print(f"Hello World! from pylib version: {{{cookiecutter.project_slug}}.__version__}")


if __name__ == "__main__":
    main()
