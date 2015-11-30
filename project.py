import project_map


def main():
    print('====================Python Pokemon====================')
    player = project_map.player
    player.location = project_map.oak
    print(command_help())
    print(player.location)
    command = input('>>> ').lower().split()
    while not command:
        command = input('>>> ').lower().split()
    while command[0] != 'quit':
        if command[0] == 'look':
            print(player.location)
        elif command[0] == 'health':
            print('\nPlayer health: {} hp\n'.format(player.health))
        elif command[0] == 'go':
            player.go_to(command)
        elif command[0] == 'help':
            print(command_help())
        elif command[0] == 'get':
            player.add_to_inventory(command)
        elif command[0] == 'drop':
            player.remove_from_inventory(command)
        elif command[0] == 'list':
            print(player)
        elif command[0] == 'use':
            player.use(command)
        elif command[0] == 'moves':
            if player.weapon == None:
                print('\nYou have not chosen a pokemon!\n')
            else:
                print(player.weapon.name + ' ' + str(
                    player.weapon.damage))
        elif command[0] == 'choose':
            if player.weapon != None:
                player.inventory.append(player.weapon)
            player.wield(command)
        elif command[0] == 'attack' or command[0] == 'kill':
            if player.weapon == None:
                print('\nYou have not chosen a pokemon!\n')
            elif len(command) < 2:
                print('\n{} what?\n'.format(
                    command[0][0].upper() + command[0][1:]))
            elif len(command) < 3:
                print('\nWhat move {}?\n'.format(player.weapon.damage))
            elif len(command) < 4:
                player.attack([command[0], command[1]], command[2])
        else:
            print('\nI don\'t understand you.\n')
        project_map.move_others()
        if player.health <= 0:
            print('\nGAME OVER!')
            break
        command = input('>>> ').lower().split()
        while not command:
            command = input('>>> ').lower().split()

def command_help():
    output = '\n\nCommands: go, look, list, drop, get, choose, moves,'
    output += ' attack(target then sperated by a space move), kill(same as attack command),'
    output += ' health, use, help, and quit.\n'
    return output


if __name__ == '__main__':
    main()
