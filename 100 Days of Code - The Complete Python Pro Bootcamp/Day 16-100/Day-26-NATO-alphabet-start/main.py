import pandas

natodf = pandas.read_csv("nato_phonetic_alphabet.csv")

main_dict = {row.letter: row.code for (index, row) in natodf.iterrows()}
# print(main_dict)

only_letters = False

while only_letters != True:
    user_input = input("Please type a word: ").upper()
    try:
        print_list = [main_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        only_letters = True

print(print_list)

# ---- Angela's solution using a function. Much cleaner!!! ---- #

# import pandas
#
# natodf = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# main_dict = {row.letter: row.code for (index, row) in natodf.iterrows()}
#
# def generate_phonetic():
#     user_input = input("Please type a word: ").upper()
#     try:
#         print_list = [main_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(print_list)
#
# generate_phonetic()






# ---------------- This is just some reference and test code -------------------------#

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
    #print(key, value)
    #pass


# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #print(row.student, row.score)
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}