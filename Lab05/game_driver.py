from Lab05 import Lab_05


def main():
    print("********** WELCOME, adventurer!! **********")

    syl_count = input("Forgot my glasses; can't read my attendance sheet..... how many syllables are in your name?")
    character = Lab_05.create_character(int(syl_count))

    print("********** Welcome " + character[0] + "! Announce yourself!**********")

    print("Behold! I am the mighty " + character[0] + " - scourge of a place with an equally incomprehensible name.\n")
    print("My uproarious abilities:\n")
    print('####################')

    Lab_05.print_character(character)

    print('####################')

    items_list = ["Rapier", "Broadsword", "Vorpal sword", "The constrictor", "A newt"]

    eq_count = input("********** " + character[0] + ", I have " + str(
        len(items_list)) + " items for you! But, they're secret. How many you would like?**********\n ")
    eq_count = int(eq_count) - 0  # enough of these f'ing string errors

    eq_list = []
    if eq_count > len(items_list) or eq_count <= 0:
        Lab_05.choose_inventory(items_list, eq_count)
    elif eq_count > 0:
        character.append(Lab_05.choose_inventory(items_list, eq_count))
        print("********** You are a new person! Behold, world! I give you: **********\n ")
        Lab_05.print_character(character)


if __name__ == '__main__':
    main()