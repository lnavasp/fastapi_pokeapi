from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_pokemons():
    """
        Prueba del endpoint "/" para obtener los pokemones de la primera generacion (151 pokemones)
    """
    response = client.get("/?limit=151")
    assert response.status_code == 200
    assert response.json() == {
        "Pokemones": [
            {
                "Nombre del pokemon": "bulbasaur",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/1/"
            },
            {
                "Nombre del pokemon": "ivysaur",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/2/"
            },
            {
                "Nombre del pokemon": "venusaur",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/3/"
            },
            {
                "Nombre del pokemon": "charmander",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/4/"
            },
            {
                "Nombre del pokemon": "charmeleon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/5/"
            },
            {
                "Nombre del pokemon": "charizard",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/6/"
            },
            {
                "Nombre del pokemon": "squirtle",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/7/"
            },
            {
                "Nombre del pokemon": "wartortle",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/8/"
            },
            {
                "Nombre del pokemon": "blastoise",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/9/"
            },
            {
                "Nombre del pokemon": "caterpie",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/10/"
            },
            {
                "Nombre del pokemon": "metapod",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/11/"
            },
            {
                "Nombre del pokemon": "butterfree",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/12/"
            },
            {
                "Nombre del pokemon": "weedle",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/13/"
            },
            {
                "Nombre del pokemon": "kakuna",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/14/"
            },
            {
                "Nombre del pokemon": "beedrill",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/15/"
            },
            {
                "Nombre del pokemon": "pidgey",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/16/"
            },
            {
                "Nombre del pokemon": "pidgeotto",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/17/"
            },
            {
                "Nombre del pokemon": "pidgeot",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/18/"
            },
            {
                "Nombre del pokemon": "rattata",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/19/"
            },
            {
                "Nombre del pokemon": "raticate",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/20/"
            },
            {
                "Nombre del pokemon": "spearow",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/21/"
            },
            {
                "Nombre del pokemon": "fearow",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/22/"
            },
            {
                "Nombre del pokemon": "ekans",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/23/"
            },
            {
                "Nombre del pokemon": "arbok",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/24/"
            },
            {
                "Nombre del pokemon": "pikachu",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/25/"
            },
            {
                "Nombre del pokemon": "raichu",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/26/"
            },
            {
                "Nombre del pokemon": "sandshrew",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/27/"
            },
            {
                "Nombre del pokemon": "sandslash",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/28/"
            },
            {
                "Nombre del pokemon": "nidoran-f",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/29/"
            },
            {
                "Nombre del pokemon": "nidorina",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/30/"
            },
            {
                "Nombre del pokemon": "nidoqueen",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/31/"
            },
            {
                "Nombre del pokemon": "nidoran-m",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/32/"
            },
            {
                "Nombre del pokemon": "nidorino",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/33/"
            },
            {
                "Nombre del pokemon": "nidoking",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/34/"
            },
            {
                "Nombre del pokemon": "clefairy",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/35/"
            },
            {
                "Nombre del pokemon": "clefable",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/36/"
            },
            {
                "Nombre del pokemon": "vulpix",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/37/"
            },
            {
                "Nombre del pokemon": "ninetales",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/38/"
            },
            {
                "Nombre del pokemon": "jigglypuff",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/39/"
            },
            {
                "Nombre del pokemon": "wigglytuff",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/40/"
            },
            {
                "Nombre del pokemon": "zubat",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/41/"
            },
            {
                "Nombre del pokemon": "golbat",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/42/"
            },
            {
                "Nombre del pokemon": "oddish",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/43/"
            },
            {
                "Nombre del pokemon": "gloom",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/44/"
            },
            {
                "Nombre del pokemon": "vileplume",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/45/"
            },
            {
                "Nombre del pokemon": "paras",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/46/"
            },
            {
                "Nombre del pokemon": "parasect",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/47/"
            },
            {
                "Nombre del pokemon": "venonat",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/48/"
            },
            {
                "Nombre del pokemon": "venomoth",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/49/"
            },
            {
                "Nombre del pokemon": "diglett",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/50/"
            },
            {
                "Nombre del pokemon": "dugtrio",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/51/"
            },
            {
                "Nombre del pokemon": "meowth",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/52/"
            },
            {
                "Nombre del pokemon": "persian",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/53/"
            },
            {
                "Nombre del pokemon": "psyduck",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/54/"
            },
            {
                "Nombre del pokemon": "golduck",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/55/"
            },
            {
                "Nombre del pokemon": "mankey",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/56/"
            },
            {
                "Nombre del pokemon": "primeape",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/57/"
            },
            {
                "Nombre del pokemon": "growlithe",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/58/"
            },
            {
                "Nombre del pokemon": "arcanine",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/59/"
            },
            {
                "Nombre del pokemon": "poliwag",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/60/"
            },
            {
                "Nombre del pokemon": "poliwhirl",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/61/"
            },
            {
                "Nombre del pokemon": "poliwrath",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/62/"
            },
            {
                "Nombre del pokemon": "abra",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/63/"
            },
            {
                "Nombre del pokemon": "kadabra",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/64/"
            },
            {
                "Nombre del pokemon": "alakazam",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/65/"
            },
            {
                "Nombre del pokemon": "machop",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/66/"
            },
            {
                "Nombre del pokemon": "machoke",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/67/"
            },
            {
                "Nombre del pokemon": "machamp",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/68/"
            },
            {
                "Nombre del pokemon": "bellsprout",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/69/"
            },
            {
                "Nombre del pokemon": "weepinbell",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/70/"
            },
            {
                "Nombre del pokemon": "victreebel",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/71/"
            },
            {
                "Nombre del pokemon": "tentacool",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/72/"
            },
            {
                "Nombre del pokemon": "tentacruel",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/73/"
            },
            {
                "Nombre del pokemon": "geodude",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/74/"
            },
            {
                "Nombre del pokemon": "graveler",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/75/"
            },
            {
                "Nombre del pokemon": "golem",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/76/"
            },
            {
                "Nombre del pokemon": "ponyta",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/77/"
            },
            {
                "Nombre del pokemon": "rapidash",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/78/"
            },
            {
                "Nombre del pokemon": "slowpoke",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/79/"
            },
            {
                "Nombre del pokemon": "slowbro",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/80/"
            },
            {
                "Nombre del pokemon": "magnemite",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/81/"
            },
            {
                "Nombre del pokemon": "magneton",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/82/"
            },
            {
                "Nombre del pokemon": "farfetchd",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/83/"
            },
            {
                "Nombre del pokemon": "doduo",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/84/"
            },
            {
                "Nombre del pokemon": "dodrio",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/85/"
            },
            {
                "Nombre del pokemon": "seel",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/86/"
            },
            {
                "Nombre del pokemon": "dewgong",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/87/"
            },
            {
                "Nombre del pokemon": "grimer",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/88/"
            },
            {
                "Nombre del pokemon": "muk",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/89/"
            },
            {
                "Nombre del pokemon": "shellder",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/90/"
            },
            {
                "Nombre del pokemon": "cloyster",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/91/"
            },
            {
                "Nombre del pokemon": "gastly",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/92/"
            },
            {
                "Nombre del pokemon": "haunter",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/93/"
            },
            {
                "Nombre del pokemon": "gengar",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/94/"
            },
            {
                "Nombre del pokemon": "onix",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/95/"
            },
            {
                "Nombre del pokemon": "drowzee",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/96/"
            },
            {
                "Nombre del pokemon": "hypno",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/97/"
            },
            {
                "Nombre del pokemon": "krabby",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/98/"
            },
            {
                "Nombre del pokemon": "kingler",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/99/"
            },
            {
                "Nombre del pokemon": "voltorb",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/100/"
            },
            {
                "Nombre del pokemon": "electrode",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/101/"
            },
            {
                "Nombre del pokemon": "exeggcute",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/102/"
            },
            {
                "Nombre del pokemon": "exeggutor",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/103/"
            },
            {
                "Nombre del pokemon": "cubone",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/104/"
            },
            {
                "Nombre del pokemon": "marowak",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/105/"
            },
            {
                "Nombre del pokemon": "hitmonlee",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/106/"
            },
            {
                "Nombre del pokemon": "hitmonchan",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/107/"
            },
            {
                "Nombre del pokemon": "lickitung",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/108/"
            },
            {
                "Nombre del pokemon": "koffing",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/109/"
            },
            {
                "Nombre del pokemon": "weezing",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/110/"
            },
            {
                "Nombre del pokemon": "rhyhorn",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/111/"
            },
            {
                "Nombre del pokemon": "rhydon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/112/"
            },
            {
                "Nombre del pokemon": "chansey",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/113/"
            },
            {
                "Nombre del pokemon": "tangela",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/114/"
            },
            {
                "Nombre del pokemon": "kangaskhan",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/115/"
            },
            {
                "Nombre del pokemon": "horsea",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/116/"
            },
            {
                "Nombre del pokemon": "seadra",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/117/"
            },
            {
                "Nombre del pokemon": "goldeen",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/118/"
            },
            {
                "Nombre del pokemon": "seaking",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/119/"
            },
            {
                "Nombre del pokemon": "staryu",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/120/"
            },
            {
                "Nombre del pokemon": "starmie",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/121/"
            },
            {
                "Nombre del pokemon": "mr-mime",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/122/"
            },
            {
                "Nombre del pokemon": "scyther",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/123/"
            },
            {
                "Nombre del pokemon": "jynx",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/124/"
            },
            {
                "Nombre del pokemon": "electabuzz",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/125/"
            },
            {
                "Nombre del pokemon": "magmar",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/126/"
            },
            {
                "Nombre del pokemon": "pinsir",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/127/"
            },
            {
                "Nombre del pokemon": "tauros",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/128/"
            },
            {
                "Nombre del pokemon": "magikarp",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/129/"
            },
            {
                "Nombre del pokemon": "gyarados",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/130/"
            },
            {
                "Nombre del pokemon": "lapras",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/131/"
            },
            {
                "Nombre del pokemon": "ditto",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/132/"
            },
            {
                "Nombre del pokemon": "eevee",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/133/"
            },
            {
                "Nombre del pokemon": "vaporeon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/134/"
            },
            {
                "Nombre del pokemon": "jolteon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/135/"
            },
            {
                "Nombre del pokemon": "flareon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/136/"
            },
            {
                "Nombre del pokemon": "porygon",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/137/"
            },
            {
                "Nombre del pokemon": "omanyte",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/138/"
            },
            {
                "Nombre del pokemon": "omastar",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/139/"
            },
            {
                "Nombre del pokemon": "kabuto",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/140/"
            },
            {
                "Nombre del pokemon": "kabutops",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/141/"
            },
            {
                "Nombre del pokemon": "aerodactyl",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/142/"
            },
            {
                "Nombre del pokemon": "snorlax",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/143/"
            },
            {
                "Nombre del pokemon": "articuno",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/144/"
            },
            {
                "Nombre del pokemon": "zapdos",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/145/"
            },
            {
                "Nombre del pokemon": "moltres",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/146/"
            },
            {
                "Nombre del pokemon": "dratini",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/147/"
            },
            {
                "Nombre del pokemon": "dragonair",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/148/"
            },
            {
                "Nombre del pokemon": "dragonite",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/149/"
            },
            {
                "Nombre del pokemon": "mewtwo",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/150/"
            },
            {
                "Nombre del pokemon": "mew",
                "Recurso de datos": "https://pokeapi.co/api/v2/pokemon/151/"
            }
        ]
    }

def test_get_pokemon_data_by_name():
    """
        Prueba del endpoint "/" con el parametro "name" y devuelva los datos correctos para pikachu.
    """
    pokemon_name = 'pikachu'
    response = client.get(f"/?name={pokemon_name}")
    assert response.status_code == 200
    assert response.json() == {
        "Nombre del pokemon": "pikachu",
        "Habilidades": [
            "static",
            "lightning-rod"
        ],
        "Número de la pokedex": 25,
        "Sprites": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
            "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/25.png",
            "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/25.png",
            "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/25.png",
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
            "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png",
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png",
            "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/25.png",
            "other": {
            "dream_world": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/25.svg",
                "front_female": None
            },
            "home": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/female/25.png"
            },
            "official-artwork": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/25.png"
            }
            },
            "versions": {
            "generation-i": {
                "red-blue": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/25.png",
                "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/25.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/25.png",
                "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/25.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/25.png"
                },
                "yellow": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/25.png",
                "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/25.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/back/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/25.png",
                "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/25.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/25.png"
                }
            },
            "generation-ii": {
                "crystal": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/25.png",
                "back_shiny_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/shiny/25.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/25.png",
                "front_shiny_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/shiny/25.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/25.png"
                },
                "gold": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/25.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/transparent/25.png"
                },
                "silver": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/25.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/transparent/25.png"
                }
            },
            "generation-iii": {
                "emerald": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/25.png"
                },
                "firered-leafgreen": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/shiny/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/shiny/25.png"
                },
                "ruby-sapphire": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/shiny/25.png"
                }
            },
            "generation-iv": {
                "diamond-pearl": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/25.png",
                "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/female/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/25.png",
                "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/female/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/female/25.png"
                },
                "heartgold-soulsilver": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/25.png",
                "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/female/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/25.png",
                "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/female/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/female/25.png"
                },
                "platinum": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/25.png",
                "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/female/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/25.png",
                "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/female/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/female/25.png"
                }
            },
            "generation-v": {
                "black-white": {
                "animated": {
                    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/25.gif",
                    "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/female/25.gif",
                    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/25.gif",
                    "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/female/25.gif",
                    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/25.gif",
                    "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/female/25.gif",
                    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/25.gif",
                    "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/female/25.gif"
                },
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/25.png",
                "back_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/female/25.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/shiny/25.png",
                "back_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/shiny/female/25.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/shiny/female/25.png"
                }
            },
            "generation-vi": {
                "omegaruby-alphasapphire": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/female/25.png"
                },
                "x-y": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/shiny/female/25.png"
                }
            },
            "generation-vii": {
                "icons": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/25.png",
                "front_female": None
                },
                "ultra-sun-ultra-moon": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/female/25.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/25.png",
                "front_shiny_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/female/25.png"
                }
            },
            "generation-viii": {
                "icons": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/25.png",
                "front_female": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/female/25.png"
                }
            }
            }
        },
        "Tipo": [
            "electric"
        ]
    }

def test_get_pokemon_data_by_id():
    """
        Prueba del endpoint "/" con el parametro "id" y devuelva los datos correctos para new.
    """
    pokemon_id = 151
    response = client.get(f"/?id={pokemon_id}")
    assert response.status_code == 200
    assert response.json() == {
        "Nombre del pokemon": "mew",
        "Habilidades": [
            "synchronize"
        ],
        "Número de la pokedex": 151,
        "Sprites": {
            "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/151.png",
            "back_female": None,
            "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/151.png",
            "back_shiny_female": None,
            "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
            "front_female": None,
            "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/151.png",
            "front_shiny_female": None,
            "other": {
            "dream_world": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/151.svg",
                "front_female": None
            },
            "home": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/151.png",
                "front_shiny_female": None
            },
            "official-artwork": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/151.png"
            }
            },
            "versions": {
            "generation-i": {
                "red-blue": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/151.png",
                "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/151.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/151.png",
                "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/151.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/151.png"
                },
                "yellow": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/151.png",
                "back_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/151.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/back/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/151.png",
                "front_gray": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/151.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/151.png"
                }
            },
            "generation-ii": {
                "crystal": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/151.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/151.png",
                "back_shiny_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/shiny/151.png",
                "back_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/151.png",
                "front_shiny_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/shiny/151.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/151.png"
                },
                "gold": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/151.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/151.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/transparent/151.png"
                },
                "silver": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/151.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/151.png",
                "front_transparent": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/transparent/151.png"
                }
            },
            "generation-iii": {
                "emerald": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/emerald/shiny/151.png"
                },
                "firered-leafgreen": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/151.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/back/shiny/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/firered-leafgreen/shiny/151.png"
                },
                "ruby-sapphire": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/151.png",
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/back/shiny/151.png",
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/151.png",
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iii/ruby-sapphire/shiny/151.png"
                }
            },
            "generation-iv": {
                "diamond-pearl": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/151.png",
                "back_female": None,
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/back/shiny/151.png",
                "back_shiny_female": None,
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/diamond-pearl/shiny/151.png",
                "front_shiny_female": None
                },
                "heartgold-soulsilver": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/151.png",
                "back_female": None,
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/back/shiny/151.png",
                "back_shiny_female": None,
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/heartgold-soulsilver/shiny/151.png",
                "front_shiny_female": None
                },
                "platinum": {
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/151.png",
                "back_female": None,
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/back/shiny/151.png",
                "back_shiny_female": None,
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/shiny/151.png",
                "front_shiny_female": None
                }
            },
            "generation-v": {
                "black-white": {
                "animated": {
                    "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/151.gif",
                    "back_female": None,
                    "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/shiny/151.gif",
                    "back_shiny_female": None,
                    "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/151.gif",
                    "front_female": None,
                    "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/151.gif",
                    "front_shiny_female": None
                },
                "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/151.png",
                "back_female": None,
                "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/back/shiny/151.png",
                "back_shiny_female": None,
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/shiny/151.png",
                "front_shiny_female": None
                }
            },
            "generation-vi": {
                "omegaruby-alphasapphire": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/151.png",
                "front_shiny_female": None
                },
                "x-y": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/shiny/151.png",
                "front_shiny_female": None
                }
            },
            "generation-vii": {
                "icons": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/icons/151.png",
                "front_female": None
                },
                "ultra-sun-ultra-moon": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/151.png",
                "front_female": None,
                "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/151.png",
                "front_shiny_female": None
                }
            },
            "generation-viii": {
                "icons": {
                "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-viii/icons/151.png",
                "front_female": None
                }
            }
            }
        },
        "Tipo": [
            "psychic"
        ]
    }

def test_update_pokemon_data():
    """
        Prueba del endpoint "/update_pokemon" prueba donde se quiere modificar la informacion del pokemon "pikachu"
        Para esto se usa el id del pokemon
            id: 25
        informacion a actualizar
            pokemon_name: "Super Pikachu"
            pokemon_abilities: "Hiper rayo"
            pokemon_sprites: "https://co.pinterest.com/pin/729935052097368076/"
            pokemon_type: "Normal"
    """
    pokemon_id = 25
    pokemon_name = "Super Pikachu"
    pokemon_abilities = "Hiper rayo"
    pokemon_sprites = "https://co.pinterest.com/pin/729935052097368076/"
    pokemon_type = "Normal"
    response = client.get(f"/update_pokemon?id={pokemon_id}&name={pokemon_name}&abilities={pokemon_abilities}&sprites={pokemon_sprites}&type={pokemon_type}")
    assert response.status_code == 200
    assert response.json() == {
        "Nombre del pokemon": "Super Pikachu",
        "Habilidades": "Hiper rayo",
        "Número de la pokedex": 25,
        "Sprites": "https://co.pinterest.com/pin/729935052097368076/",
        "Tipo": "Normal"
    }

def test_get_pokemons_not_found():
    """
        Prueba endpoint "/" con un id de pokemon que no existe
    """
    pokemon_id = 2000
    response = client.get(f"/?id={pokemon_id}")
    assert response.status_code == 404

def test_get_pokemon_data_not_found():
    """
        Prueba endpoint "/" con nombre incorrecto del pokemon
    """
    pokemon_name = "Pikachu"
    response = client.get(f"/?name={pokemon_name}")
    assert response.status_code == 404