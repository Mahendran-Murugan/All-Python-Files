def roman_to_numeric(roman):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeric = 0
    for i in range(0, len(roman)):
        try:
            if i < len(roman) and rom_val[roman[i]] >= rom_val[roman[i + 1]]:
                numeric += rom_val[roman[i]]
            elif i < len(roman) and rom_val[roman[i]] < rom_val[roman[i + 1]]:
                numeric -= rom_val[roman[i]]
        except Exception as e:
            numeric += rom_val[roman[i]]
    print("The corresponding numeric value:", numeric)


for _ in range(int(input())):
    in_str = input("Enter your Roman value:").upper()
    roman_to_numeric(in_str)
