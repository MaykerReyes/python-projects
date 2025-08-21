
import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    """Fetches data for a given Pokémon by name."""
    url = f"{BASE_URL}/pokemon/{name.lower()}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Pokémon not found: {name}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    return None

def display_pokemon_info(pokemon):
    print(f"\nName: {pokemon['name'].capitalize()}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
    print("Types:")
    for type_info in pokemon['types']:
        print(f"  - {type_info['type']['name'].capitalize()}")
    print("Abilities:")
    for ability in pokemon['abilities']:
        print(f"  - {ability['ability']['name'].replace('-', ' ').capitalize()}")

def main():
    name = input("Enter the name of a Pokémon: ").strip()
    if not name:
        print("No name entered.")
        return
    pokemon = get_pokemon_info(name)
    if pokemon:
        display_pokemon_info(pokemon)

if __name__ == "__main__":
    main()
