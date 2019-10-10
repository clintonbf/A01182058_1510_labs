from Lab05 import Lab_05


def main():
    print("********** WELCOME, adventurer!! **********")

    syl_count = input("Forgot my glasses; can't read my attendance sheet..... how many syllables are in your name?")
    character = Lab_05.create_character(int(syl_count))

    print("********** Welcome " + character[0] + "!**********")

    eq_count = input("********** I have 4 items for you! How many you would like?********** ")
    items_list = ["rapier", "broadsword (which isn't what you think it is)", "vorpal sword (vorp!)",
                  "Coding the gregarious's python"]

    character.append(Lab_05.choose_inventory(items_list, int(eq_count)))

    Lab_05.print_character(character)


if __name__ == '__main__':
    main()