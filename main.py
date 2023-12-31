from fastapi import FastAPI, Query, HTTPException
import httpx

app = FastAPI()

def get_custom_pokemon_data(response: dict, name=None, abilities=None, id=None, sprites=None, type=None):
    """
        Esta funcion organiza la informacion del pokemon segun tempate
            "Nombre del pokemon":
            "Habilidades":
            "Número de la pokedex":
            "Sprites":
            "Tipo":
    """
    data = {
        "Nombre del pokemon": name if name is not None else response["name"],
        "Habilidades": abilities if abilities is not None else [pokemon["ability"]["name"] for pokemon in response["abilities"]],
        "Número de la pokedex": id if id is not None else response["id"],
        "Sprites": sprites if sprites is not None else response["sprites"],
        "Tipo": type if type is not None else [pokemon["type"]["name"] for pokemon in response["types"]],
    }
    return data

@app.get("/")
async def get_pokemon(
    id: int = Query(None, title="Pokedex ID", description="ID del pokedex", gt=0),
    name: str = Query(None, title="Nombre del pokemon", description="Nombre del pokemon"),
    limit: int = Query(None, title="limit", description="limit", gt=0),
):
    """
        endpoint "/" con 3 parametros opcionales: id, name, limit
            1- Si se pasa el parámetro 'id' devuelve los datos del pokemon correspondiente
            2- Si se pasa el parámetro 'name' devuelve los datos del pokemon correspondiente
            3- Si se pasa el parámetro 'limit' devuelve el numero de pokemones especificados
            4- En caso de no pasar ningun parametro, devuelve todos los pokemones
    """
    base_url = "https://pokeapi.co/api/v2/pokemon"
    if id is not None:
        base_url += f"/{id}"
    elif name is not None:
        base_url += f"/{name}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(base_url)
            response.raise_for_status()
            pokemon_data = response.json()
            if id or name is not None:
                data = {
                    "Nombre del pokemon": pokemon_data["name"],
                    "Habilidades": [pokemon["ability"]["name"] for pokemon in pokemon_data["abilities"]],
                    "Número de la pokedex": pokemon_data["id"],
                    "Sprites": pokemon_data["sprites"],
                    "Tipo": [pokemon["type"]["name"] for pokemon in pokemon_data["types"]],
                }
            else:
                response = await client.get(base_url + f"?limit={limit if limit else pokemon_data['count']}")
                response.raise_for_status()
                pokemon_data = response.json()
                data = {
                    "Pokemones": [{"Nombre del pokemon": pokemon["name"], "Recurso de datos": pokemon["url"]} for pokemon in pokemon_data["results"]]
                }
            return data
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error al obtener datos del Pokémon")

@app.get("/update_pokemon")
async def update_pokemon_data(
    id: int = Query(title="Pokedex ID", description="ID del pokedex", gt=0),
    name: str = Query(None, title="Nombre del pokemon", description="Nombre del pokemon"),
    abilities: str = Query(None, title="Habilidades del pokemon", description="Habilidades del pokemon"),
    sprites: str = Query(None, title="sprites del pokemon", description="sprites del pokemon"),
    type: str = Query(None, title="Tipo del pokemon", description="Tipo del pokemon"),
):
    """
        endpoint "/update_pokemon" con 1 parametro obligatorio y 4 parametros opcionales, Este endpoint permite modificar la informacion de pokemon
        parametros:
        1- id: Obligatorio se usa para buscar el pokemon
        2- name: Opcional parametro para modificar informacion 
        3- abilities: Opcional parametro para modificar informacion 
        4- sprites: Opcional parametro para modificar informacion 
        5- type: Opcional parametro para modificar informacion 
    """
    base_url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(base_url)
            response.raise_for_status()
            pokemon_data = response.json()
            data = get_custom_pokemon_data(pokemon_data, name=name, abilities=abilities, sprites=sprites, type=type)
            return data
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Error al obtener datos del Pokémon")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
