class AClass:
    """A simple python class."""

    def __init__(self, name: str) -> None:
        """
        Intialize new class object.

        :param name: The name of the class
        """
        self.name = name

    def action(self) -> None:
        """Print the name of the class."""
        print(f"Hello, I'm a {self.name} class")

    def change_name(self, name: str) -> None:
        """
        Change the name of the class.

        :param name: The new name
        """
        self.name = name
