def allLongestStrings(inputArray):
    longest = 0
    for String in inputArray:
        if len(String) > longest:
            longest = len(String)
    LongestString = []

    for String in inputArray:
        if len(String) == longest:
            LongestString.append(String)
    return LongestString
