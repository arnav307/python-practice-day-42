def substring(s):
    letters = []  
    max_length = 0  
    start = 0 

    for char in s:
        if char in letters:
            
            start = letters.index(char) + 1
            letters = letters[start:]  
        letters.append(char)
        max_length = max(max_length, len(letters))  
    return max_length


s = "abcabcbb"
print(substring(s))  