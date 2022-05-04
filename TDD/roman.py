def roman2int(roman:str):
    for letter in roman:
        if letter not in ("X","I","V"):
            print(roman)
            raise ValueError