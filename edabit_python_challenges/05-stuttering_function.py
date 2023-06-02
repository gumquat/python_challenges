def stuttering_function(word):
    first_two_letters = word[:2]
    stuttered_word = "{}...{}...{}?".format(first_two_letters, first_two_letters, word)
    return stuttered_word

print("The input word is 'Stuttering'")
print(stuttering_function("Stuttering"))
