from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


default_things=[
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
    )
]