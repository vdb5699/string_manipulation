def replacing_string_space(string, replacer):
    try:
        result = ''
        for letter in string:
            if letter == ' ':
                print(letter)
                letter = replacer
                # print(f"Replaced {string[letter]} with {replacer}")
            result += letter
        print(result)
        return result
    except TypeError:
        print('needs to be string')


def reversing_string(string):
    try:
        result = ''
        for letter in reversed(string):
            result += letter
        return result
    except TypeError:
        print('needs to be string')


def check_palindrome(string):
    try:
        testing_word = reversing_string(string)
        if string == testing_word:
            print(f"__{string}__ is a Palindrome")
            return True
        else:
            print(f"__{string}__ is not a Palindrome")
            return False
    except TypeError:
        print("Needs to be String")


if __name__ == '__main__':
    # word = 'n 1test'
    reverse_word_1 = 'racecar'
    reverse_word_2 = 'reverse'
    # replacing_letter = '0'
    # final_word = replacing_string_space(word, replacing_letter)
    # print(f"Initial string: {word} \nFinal string: {final_word}")
    # print(f"Reversed String: {reversing_string(reverse_word)}")
    print(f"Palindrome Check: {check_palindrome(reverse_word_1)}")
    print(f"Palindrome Check: {check_palindrome(reverse_word_2)}")