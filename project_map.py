from project_class import Room
from project_class import Pokemon
from project_class import Trainer
import random

v_city = Room('Viridian City', {}, [])
route_1 = Room('Route 1', {}, [])
route_2 = Room('Route 2', {}, [])
oak = Room('Oak\'s office', {}, [])
broom = Room('Broom closet', {}, [])
v_city_mart = Room('Viridian City Mart', {}, [])
v_city_gym = Room('Viridian City Gym!', {}, [])
v_forest1 = Room('Viridian Forest 1', {}, [])
v_forest2 = Room('Viridian Forest 2', {}, [])
v_forest3 = Room('Viridian Forest 3', {}, [])
v_forest4 = Room('Viridian Forest 4', {}, [])
v_forest5 = Room('Viridian Forest 5', {}, [])
v_forest6 = Room('Viridian Forest 6', {}, [])
p_city = Room('Pewter City', {}, [])
p_city_mart = Room('Pewter City Mart', {}, [])
# pcg = 'pewter city gym'
pcg1 = Room('Pewter City Gym Room 1', {}, [])
pcg2 = Room('Pewter City Gym Room 2', {}, [])
pcg3 = Room('Pewter City Gym Room 3', {}, [])
pcg4 = Room('Pewter City Gym Room 4', {}, [])
pcg5 = Room('Pewter City Gym Room 5', {}, [])
pcg6 = Room('Pewter City Gym Room 6', {}, [])
pcg7 = Room('Pewter City Gym Room 7', {}, [])
pcg8 = Room('Pewter City Gym Room 8', {}, [])
brock = Room('Pewter City Gym\'s Trainer Room!', {}, [])

oak.doors({'north': route_1, 'east': broom})
broom.doors({'west': oak})
route_1.doors({'south': oak, 'north': v_city})
v_city.doors({'south': route_1, 'north': route_2, 'east': v_city_gym, 'west': v_city_mart})
route_2.doors({'south': v_city, 'north': v_forest2})
v_city_mart.doors({'east': v_city})
v_city_gym.doors({'west': v_city})
v_forest1.doors({'north': v_forest6, 'east': v_forest2})
v_forest2.doors({'north': v_forest5, 'east': v_forest3, 'west': v_forest1, 'south': route_2})
v_forest3.doors({'north': v_forest4, 'west': v_forest2})
v_forest4.doors({'south': v_forest3, 'west': v_forest5})
v_forest5.doors({'south': v_forest2, 'west': v_forest6, 'east': v_forest4})
v_forest6.doors({'south': v_forest1, 'east': v_forest5})
p_city.doors({'north': pcg1, 'east': p_city_mart})
p_city_mart.doors({'west': p_city})
# pcg = 'pewter city gym'
pcg1.doors({'south': p_city, 'north': pcg4, 'west': pcg2})
pcg2.doors({'north': pcg3, 'east': pcg1})
pcg3.doors({'south': pcg2, 'north': pcg6, 'east': pcg4})
pcg4.doors({'south': pcg1, 'north': pcg5, 'west': pcg3})
pcg5.doors({'south': pcg4, 'north': pcg8, 'west': pcg6})
pcg6.doors({'south': pcg3, 'north': pcg7, 'east': pcg5})
pcg7.doors({'south': pcg6, 'east': pcg8})
pcg8.doors({'south': pcg5, 'north': brock, 'west': pcg7})
brock.doors({'south': pcg8})

potion = Potion('potion', 'heals for 20 health', 20)
super_potion = Potion('super_potion', 'heals for 50 health', 50)

starters = []
bulb = Pokemon('bulbasaur', route_1, {'absorb': 5}, 'gary\'s grass starter')
squirt = Pokemon('squirtle', route_1, {'bubble': 5}, 'gary\'s water starter')
charm = Pokemon('charmander', route_1, {'ember': 5}, 'gary\'s fire starter')
weedle2 = Pokemon('weedle', v_forest1, {'poisonsting': 20}, 'bryce\'s hairy bug pokemon')
pika = Pokemon('pikachu', route_2, {'volttackle': 20}, 'mike\'s pikachu')
scyth = Pokemon('scyther', v_forest6, {'slash': 35}, 'dillon\'s mantis pokemon')
cubone = Pokemon('cubone', pcg7, {'bonemerang': 36}, 'grant\'s lonely pokemon')
onix = Pokemon('onix', brock, {'irontail': 40,}, 'brock\'s rock snake pokemon')
diglett = Pokemon('diglett', pcg4, {'dig': 35,}, 'david\'s mole pokemon')
butterfree = Pokemon('butterfree', v_forrest6, {'charm': 1}, 'zak\'s butterfly pokemon')

bulbasaur = Pokemon('bulbasaur', oak, {'absorb': 20}, 'The grass starter')
squirtle = Pokemon('squirtle', oak, {'bubble': 20}, 'The water starter')
charmander = Pokemon('charmander', oak, {'ember': 20}, 'The fire starter')
mew = Pokemon('mew', broom, {'psychic': 60, 'megapunch': 50}, 'mysterious pokemon')
pidgey = Pokemon('pidgey', route_1, {'gust': 20, 'tackle': 15}, 'tiny bird pokemon')
rattata = Pokemon('rattata', route_1, {'tackle': 20}, 'mouse pokemon')
caterpie = Pokemon('caterpie', v_forest2, {'tackle': 20}, 'worm pokemon')
weedle = Pokemon('weedle', v_forest2, {'posionsting': 20}, 'hairy bug pokemon')
metapod = Pokemon('metapod', v_forest3, {'harden': 5}, 'cocoon pokemon')
kakuna = Pokemon('kakuna', v_forest5, {'harden': 5}, 'cocoon  pokemon')
scyther = Pokemon('scyther', v_forest6, {'slash': 35, 'cut': 20}, 'mantis pokemon')
pikachu = Pokemon('pikachu', v_forest6, {'volttackle': 30, 'tackle': 20}, 'mouse  pokemon')

oak.add_pokemon(bulbasaur)
oak.add_pokemon(squirtle)
oak.add_pokemon(charmander)
broom.add_pokemon(mew)
starters.append(bulb)
starters.append(squirt)
starters.append(charm)

p_city_mart.add_pokemon(potion)
p_city_mart.add_pokemon(potion)
p_city_mart.add_pokemon(potion)
p_city_mart.add_pokemon(potion)
p_city_mart.add_pokemon(potion)
p_city_mart.add_pokemon(super_potion)
v_city_mart.add_pokemon(potion)
v_city_mart.add_pokemon(potion)
v_city_mart.add_pokemon(potion)
v_city_mart.add_pokemon(potion)
v_city_mart.add_pokemon(potion)
v_city_mart.add_pokemon(super_potion)
broom.add_pokemon(super_potion)

player = Trainer('ash')

rb1 = Trainer('gary')
rb1.weapon = random.choice(starters)
rb1.location = route_1
rb1.inventory = [potion] 

bt1 = Trainer('bug_trainer_bryce')
bt1.weapon = weedle2
bt1.location = v_forrest1

bt2 = Trainer('bug_trainer_dillon')
bt2.weapon = scyth
bt2.location = v_forrest4
bt2.inventory = [potion]

bt3 = Trainer('bug_trainer_zak')
bt3.weapon = butterfree
bt3.location = v_forrest6
bt3.inventory = [potion]

at2 = Trainer('ace_trainer_mike')
at2.weapon = pika
at2.location = route_2
at2.inventory = [super_potion]

hik = Trainer('hiker_david')
hik.weapon = diglett
hik.location = pcg4
hik.inventory = [potion]

at1 = Trainer('ace_trainer_grant')
at1.weapon = cubone
at1.location = pcg7
at1.inventory = [super_potion]

gl = Trainer('gym_leader_brock')
gl.weapon = onix
gl.location = brock
gl.inventory = [super_potion]

trainer_list = []
a = list(globals().values())
for item in a:
    if isinstance(item, Trainer):
        trainer_list.append(item)
        
def move_others():
    for et in trainer_list:
        if et.name != 'ash' and et.location == player.location:
            print('\nTrainer {} challenges you!\n'.format(et.name))
            move = et.weapon.damage.keys()
            if 'absorb' in move:
                et.attack(['attack', 'ash'], 'absorb')
            elif 'bubble' in move:
                et.attack(['attack', 'ash'], 'bubble')
            elif 'ember' in move:
                et.attack(['attack', 'ash'], 'ember')
            elif 'posionsting' in move:
                et.attack(['attack', 'ash'], 'posionsting')
            elif 'slash' in move:
                et.attack(['attack', 'ash'], 'slash')
            elif 'charm' in move:
                et.attack(['attack', 'ash'], 'charm')
            elif 'volttackle' in move:
                et.attack(['attack', 'ash'], 'volttackle')
            elif 'dig' in move:
                et.attack(['attack', 'ash'], 'dig')
            elif 'bonemerang' in move:
                et.attack(['attack', 'ash'], 'bonemerang')
            elif 'irontail' in move:
                et.attack(['attack', 'ash'], 'irontail')

