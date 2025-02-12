from model import Creature

_creatures: list[Creature] = [
    Creature(
        name='Yeti',
        country='CN',
        area='Himalayas',
        description='Big white smelly humanoid',
        aka="Snow man"
    ),
    Creature(
        name='Grandma Yaga',
        country="RU",
        area="Slavic woods",
        description='Old one-legged witch from wood, eats children',
        aka="Bon Leg"
    ),
    Creature(
        name='Koshchei Immortal',
        country="RU",
        area="Far peopleless lands",
        description='Old thin pedofil, with death inside the egg',
        aka="Immortal"
    )
]


def get_creatures() -> list[Creature]:
    return _creatures
