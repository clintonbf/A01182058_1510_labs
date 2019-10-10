from Lab05 import Lab_05


def main():
    print("********** WELCOME, adventurer!! **********")

    syl_count = input("Forgot my glasses; can't read my attendance sheet..... how many syllables are in your name?")
    character = Lab_05.create_character(int(syl_count))

    print("Ah! Welcome " + character[0])

    print("********** I shall look into your soul, and tell you your qualities! **********")

    # attributes = Lab_05.


if __name__ == '__main__':
    main()
