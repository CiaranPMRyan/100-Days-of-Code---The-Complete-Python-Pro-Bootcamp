PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt", "r") as name_doc:
    names = name_doc.readlines()
    print(names)

with open("./input/Letters/starting_letter.txt", "r") as letter:
    body = letter.read()
    for name in names:
        clean_name = name.strip()
        new_letter = body.replace("[name]", f"{clean_name}")
        print(new_letter)
        with open(f"Output/ReadyToSend/Letter_For_{clean_name}.txt", "x") as new_file:
            new_file.write(new_letter)

