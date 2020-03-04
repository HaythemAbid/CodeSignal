def arrayChange(inputArray):
    sum = 0
    int = inputArray[0]
    for i in inputArray[1:]:
        if i <= int:
            sum += int - i + 1
            int = int + 1
        else:
            int = i
    return sum
