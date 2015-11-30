import project_map
import random


class Room():
    
    exits = {}
    name = ''
    pokemons = []

    def __init__(self, name, exits, pokemons):
        self.name = name
        self.exits = exits
        self.pokemons = pokemons


    def doors(self, outside):
        self.exits = outside


    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)


    def remove_pokemon(self, thing):
        self.pokemons.remove(thing)


    def __str__(self):
        output = '\nYou\'re in {}.\n'.format(self.name)
        for char in project_map.trainer_list:
            if char.name != 'ash':
                if char.location.name == self.name:
                    output += '\n{} the trainer is here!\n\n'.format(
                        char.name)
        output += 'You can see exits: '
        for key in self.exits:
            output += '\n    {} ({})'.format(key, self.exits[key].name)
        if self.pokemons:
            output += '\n\nThe room contains:\n'
            for pokemon in self.pokemons:
                output += '    {}, {}\n'.format(pokemon.name,
                                                pokemon.examine())
        else:
            output += '\n'
        return output


class Pokemon:
    
    name = ''
    description = ''
    location = ''
    damage = {}


    def __init__(self, name, location, damage, description):
        self.name = name
        self.location = location
        self.description = description
        self.damage = damage


    def __str__(self):
        output = 'name: {}, damage: {}, location: {}, \
description: {}'.format(self.name,
                        self.damage,
                        self.location.name,
                        self.description)
        return output


    def examine(self):
        return(self.description)


    def drop(self, room):
        self.location = room


class Potion():
    name = ''
    description = ''
    modifier = 0
    
    def __init__(self, name, description, modifier):
        self.name = name
        self.description = description
        self.modifier = modifier
        
    def __str__(self):
        output = 'name: {}, description: {}, \
        modifier: {}'.format(self.name, self.description, self.modifier)
        return output
        
    def examine(self):
        return self.description


class Trainer():
    name = ''
    health = 0
    weapon = 0
    location = None
    inventory = []

    def __init__(self, name):
        self.inventory = []
        self.name = name
        self.health = 100
        self.location = None
        self.weapon = None


    def __str__(self):
        output = ''
        if self.inventory:
            for item in self.inventory:
                output += item.__str__()
        if self.weapon:
            output += 'Using: {} - {}\n'.format(
                self.weapon.name, self.weapon.description)
        if output:
            output = '\nInventory:\n' + output
        else:
            output = '\nYour pockets are empty.\n'
        return output


    def go_to(self, command):
        if len(command) > 1:
            if command[1] in self.location.exits.keys():
                self.location = self.location.exits[command[1]]
                print(self.location)
            else:
                print('\nYou can\'t go that way!\n')
        else:
            print('\nGo where?\n')


    def add_to_inventory(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        for item in self.location.pokemons:
            if command[1] == item.name:
                self.inventory.append(item)
                self.location.pokemons.remove(item)
                print('\nOkay.\n')
                return
        else:
            print('\nThere\'s no {} here!\n'.format(command[1]))
            return


    def remove_from_inventory(self, command):
        if len(command) < 2:
            print('\nDrop what?\n')
        else:
            if self.weapon and command[1] == self.weapon.name:
                self.location.pokemons.append(self.weapon)
                self.weapon = None
                print('\nOkay.\n')
                return
            else:
                for item in self.inventory:
                    if command[1] == item.name:
                        self.location.pokemons.append(item)
                        self.inventory.remove(item)
                        print('\nOkay.\n')
                        return
                    else:
                        print('\nYou don\'t have that!\n')
    def use(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        for thing in self.inventory:
            if command[1] == thing.name:
                self.health += thing.modifier
                if self.health > 100:
                    self.health = 100
                self.inventory.remove(thing)
                print('\nYou used a {}.\n'.format(
                    thing.name))
                return
        else:
            print('\nYou don\'t have that!\n')

    def wield(self, command):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        for thing in self.inventory:
            if command[1] == thing.name:
                self.weapon = thing
                self.inventory.remove(thing)
                print('\nYou choose {}.\n'.format(
                    thing.description))
                return
        else:
            print('\nYou don\'t have that!\n')

    def attack(self, command, move):
        if len(command) < 2:
            print('\n{} what?\n'.format(
                command[0][0].upper() + command[0][1:]))
            return
        if not self.weapon:
            print('\nYou have not chosen a pokemon!\n')
        if move not in self.weapon.damage.keys():
            print('\nMove not available!\n')
        else:
            for enemy in project_map.trainer_list:
                if enemy.name == command[1] and \
                   enemy.location == self.location:
                    damage = self.weapon.damage[move]
                    d = random.choice(range(damage - 5, damage + 10))
                    if d >= 0:
                        enemy.health -= d
                    print('\n{} has been hit for '.format(
                        enemy.name) + str(d) + '!\n')
                    if enemy.health <= 0:
                        print('\n{} has blacked out!\n'.format(enemy.name))
                        if enemy.weapon:
                            self.location.pokemons.append(enemy.weapon)
                        for item in enemy.inventory:
                            self.location.pokemons.append(item)
                        project_map.trainer_list.remove(enemy)
                        print(self.location)
                    return
            else:
                print('\n{} isn\'t here!\n'.format(command[1]))


