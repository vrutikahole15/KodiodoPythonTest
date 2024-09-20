
def count_vowels_consonants(string):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in string:
        if char.isalpha():  
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count

input_string = input("Enter a string: ")

vowels, consonants = count_vowels_consonants(input_string)


print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
