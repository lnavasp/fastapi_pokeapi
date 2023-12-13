# fastapi_pokeapi
Esta `API` funciona como `Middleware` permitiendo realizar consusltas `GET` de forma publica al `API` del profesor `OAK`. 
## Instalación
1. Instale las dependencias del archivo requirements.txt
```console
$ pip install -r requirements.txt
```
## Ejecución del servidor FastAPI
```console
$ uvicorn main:app --reload
```
## Uso del API (endopints)
### `GET /`
- Parámetros:
    1. id: Si esta definido devuelve los datos del pokemon correspondiente
    2. name: Si esta definido devuelve los datos del pokemon correspondiente
    3. limit: Si esta definido devuelve el numero de pokemones especificados
> Nota: Si no se define ningun parametro devuelve la lista de todos los pokemones
### `GET /update_pokemon`
Actualiza los datos de un Pokemon en base a ID, si no existe uno con ese ID devuelve una respuesta 404.
- Parámetros:
    1. id<span style="color: red" >*</span>: El ID del Pokemon que queremos actualizar
    2. nombre: El nuevo nombre del Pokemon
    3. abilities: La nueva Habilidad del Pokemon
    4. sprites: La nueva imagen del Pokemon
    5. type: Los nuevos tipos del Pokemon
## Pruebas unitarias
Para correr las pruebas unitarias es necesario tener instalado pytest (`incluido en requirements.txt` ) y ejecutar desde consola

```console
$ pytest test_main.py
```
