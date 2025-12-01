from app.models.pokemon import Pokemon
import hashlib

def generate_hash_id(pokemon_id: int, source: str) -> str:
    return hashlib.sha256(str(pokemon_id).encode("utf-8") + source.encode("utf-8")).hexdigest()

def transform_pokemon_data(pokemon_data, source: str) -> Pokemon | None:
    """Transform raw Pokemon data into the Pokemon model."""
    if pokemon_data is None:
        return None
    
    #change the way to get de pokemon_id depending on the source
    # id for http source
    # pokemon_id for mongo_db source 
    pokemon_id = pokemon_data["id"] if "id" in pokemon_data else pokemon_data["pokemon_id"]

    hash_id = generate_hash_id(pokemon_id, source)

    pokemon = Pokemon(
        pokemon_id=pokemon_id,
        name=pokemon_data["name"],
        height=pokemon_data["height"],
        weight=pokemon_data["weight"],
        base_experience=pokemon_data["base_experience"],
        source=source,
        hash_id=hash_id
        )
    return pokemon