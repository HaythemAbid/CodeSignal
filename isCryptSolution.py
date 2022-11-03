def solution(crypt, solution):
    
    s_dict = dict(solution)
    word1 = ''
    word2 = ''
    word3 = ''
    
    for char in crypt[0]:
        word1 += s_dict.get(char)
    if word1[0] == '0' and len(word1) !=1 :
        return False
    word1 = int(word1)
    
    for char in crypt[1]:
        word2 += s_dict.get(char)
    if word2[0] == '0' and len(word2) !=1 :
        return False
    word2 = int(word2)
    
    for char in crypt[2]:
        word3 += s_dict.get(char)
    if word3[0] == '0' and len(word3) !=1 :
        return False
    word3 = int(word3)
    
    
    return (word1 + word2) == word3
