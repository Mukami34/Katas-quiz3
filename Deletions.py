def min_deletions_to_make_even(S):
    letter_count = {}
    for char in S:
        letter_count[char] = letter_count.get(char, 0) + 1
    
    odd_count = sum(count % 2 != 0 for count in letter_count.values())
    return max(0, odd_count - 1)

print(min_deletions_to_make_even("acbcbba"))  
print(min_deletions_to_make_even("axxaxa"))  
print(min_deletions_to_make_even("aaaa"))    
