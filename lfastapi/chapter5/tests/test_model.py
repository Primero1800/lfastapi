from chapter5.model import Creature


def test_model():
    dragon = Creature(
        name="dragon",
        description=["incorrect", "string", "list"],
        country="*",
        area="*",
        aka="firedrake"
    )


if __name__ == "__main__":
    test_model()