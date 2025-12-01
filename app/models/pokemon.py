from pydantic import BaseModel


class Pokemon(BaseModel):
    hash_id: str
    pokemon_id: int
    name: str
    height: int
    weight: int
    base_experience: int
    source: str