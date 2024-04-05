# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом
# Цезаря. Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).


import string
import random


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# welcome message
print("\nWelcome\nto the Caesar's code\n")


# Enter correct string
# ________________________________________________________________
work_string = input('Work string: ')
#
# while True:
#     code = input('What we do code or decode: ').lower()
#     if code not in ['code', 'decode']:
#         print("Enter a correct code: 'code' or 'decode'")
#     else:
#         break
#
# while True:
#     language = input('Select language rus or eng: ').lower()
#     if language not in ['rus', 'eng']:
#         print("Enter a correct language: 'rus' or 'eng'")
#     else:
#         break

# while True:
#     try:
#         step_code = int(input('Step code: '))
#         break  # Если ввод является целым числом, выходим из цикла
#     except ValueError:
#         print("Enter an integer for the step code.")

# Ending check correct entered data
# ________________________________________________________________


def cesar_code(work_string, code, language):

    result_word = ''
    work_alphabet = ''
    try:
        if code == 'code':
            split_word = work_string.split()
            for count_word in split_word:
                step_count = sum(c.isalpha() for c in count_word)
                print(split_word)
                for char in count_word:
                    # print('for word in split_word', word)
                    # step_count = sum(c.isalpha() for c in word)
                    print('step_count', step_count)
                    if language == 'rus' and char in rus_upper_alphabet:
                        work_alphabet = rus_upper_alphabet
                    elif language == 'rus' and char in rus_lower_alphabet:
                        work_alphabet = rus_lower_alphabet
                    elif language == 'eng' and char in eng_upper_alphabet:
                        work_alphabet = eng_upper_alphabet
                    else:
                        work_alphabet = eng_lower_alphabet
                    if char in work_alphabet:
                        # print(word)
                        index = work_alphabet.index(char)
                        result_word += work_alphabet[(index + step_count) % len(work_alphabet)]
                    else:
                        result_word += char
                result_word += ' '
            return result_word

        # if code == 'decode':
        #     for word in work_string:
        #         if language == 'rus' and word in rus_upper_alphabet:
        #             work_alphabet = rus_upper_alphabet
        #         elif language == 'rus' and word in rus_lower_alphabet:
        #             work_alphabet = rus_lower_alphabet
        #         elif language == 'eng' and word in eng_upper_alphabet:
        #             work_alphabet = eng_upper_alphabet
        #         else:
        #             work_alphabet = eng_lower_alphabet
        #         if word in work_alphabet:
        #             # print(word)
        #             index = work_alphabet.index(word)
        #             result_word += work_alphabet[(index - step_count) % len(work_alphabet)]
        #             print(result_word)
        #         else:
        #             result_word += word

            # return result_word
    except Exception as e:
        print("An error occurred:", e)


print(cesar_code(work_string, code, language))


    # ask end or keep going program
    # ________________________________________________________________
    # user_input = input("\nDo you want to continue? (Enter 'y' to continue, 'n' to exit): ").lower()
    # if user_input == 'n':
    #     print("Program terminated.")
    #     break  # Break cycle and exit
    # elif user_input != 'y':
    #     print("Invalid input. Please enter 'y' or 'n'.\n\n")

