from Lab05 import Lab_05


def main():
    print("********** WELCOME, adventurer!! **********")

    syl_count = input("Forgot my glasses; can't read my attendance sheet..... how many syllables are in your name?")
    character = Lab_05.create_character(int(syl_count))

    print("********** Welcome " + character[0] + "!**********")

    eq_count = input("********** I have 4 items for you! How many you would like?********** ")
    eq_count = int(eq_count) - 0  # enough of these f'ing string errors

    items_list = ["rapier", "broadsword (which isn't what you think it is)", "vorpal sword (vorp!)",
                  "Coding the gregarious's python"]

    if eq_count != 0:
        eq_list = Lab_05.choose_inventory(items_list, eq_count)

    if len(eq_list) >= eq_count:
        character.append(eq_list)

    Lab_05.print_character(character)


if __name__ == '__main__':
    main()