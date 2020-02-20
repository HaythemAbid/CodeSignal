def commonCharacterCount(s1, s2):
    count=0
    List1=[char for char in s1] 
    List2=[char for char in s2] 
    for char1 in List1:
        if char1 in List2:
            count += 1
            List2.remove(char1)
    return count
