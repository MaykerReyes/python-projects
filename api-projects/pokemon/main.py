import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    """Fetches data for a given Pokémon by name."""
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        
pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print("Types:")
    for type_info in pokemon_info['types']:
        print(f"- {type_info['type']['name'].capitalize()}")    
    