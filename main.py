from src.pokeapi.sdk import PokeAPI

def main():
    # pokemon_client = PokemonClient()
    # generation_client = GenerationClient()
    #print(pokemon_client.get_pokemon("pikachu"))
    #print(generation_client.get_generation("generation-i"))

    # pokemon_client = PokemonClient()
    #print(pokemon_client.list_pokemon(limit=151, offset=0))

    api = PokeAPI()
    print(api.pokemon.get_pokemon("pikachu"))

main()