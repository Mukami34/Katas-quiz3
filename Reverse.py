def reverse_words(S):
    words = S.split()
    
    reversed_string = ' '.join(word[::-1] for word in words)
    
    return reversed_string

print(reverse_words("My name is Mary Mukami"))  
