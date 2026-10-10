# s = "anagram"
# t = "nagaram"
# def valid_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     return sorted(s) == sorted(t)
    
def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    count_t = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in t:
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1

    return count == count_t