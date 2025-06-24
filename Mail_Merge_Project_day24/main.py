PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as invitees:
    names = invitees.readlines()

with open("./input/letters/starting_letter.txt", mode="r") as letters:

    line = letters.read()
    for name in names:
        sub_name = name.strip("\n")
        x = line.replace(PLACEHOLDER, sub_name)

        with open(f"./output/readytosend/letter_for_{sub_name}.txt", mode="w") as example:
            example.write(x.strip())
