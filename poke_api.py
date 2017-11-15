import requests

BASE_URL = "http://pokeapi.co/api/v2/"

'''
URI_POKEMON_1 = "pokemon/1"

URL = BASE_URL + URI_POKEMON_1

response = requests.get(URL)

poke_dictionnary = response.json()

poke_name = poke_dictionnary['forms'][0]['name']
poke_ability = poke_dictionnary['abilities'][0]['ability']['name']
print(poke_name + "has an amazing ability: " + poke_ability)

poke_stat = poke_dictionnary['stats'][0]['stat']['name']
poke_speed_stats = poke_dictionnary['stats'][0]['base_stat']
print(str(poke_stat), ": ", poke_speed_stats)

ruby = poke_dictionnary['game_indices'][13]['version']['name']
print(ruby)
'''

poke_index = input("Which Pokemon do you want to discover? \n")

custum_uri = "pokemon/"+poke_index
custom_url = BASE_URL + custum_uri
new_response = requests.get(custom_url)

poke_dictionnary = new_response.json()
poke_name = poke_dictionnary['forms'][0]['name']
poke_moves = poke_dictionnary['moves']
print(poke_name, "has", len(poke_moves), "moves. Here's the full list of them:") 
for i in range(0,len(poke_moves)):
	poke_move_name = poke_moves[i]['move']['name']
	print(poke_move_name)