def reverseInParentheses(inputString):
    if inputString.count('(') == 0:
        return inputString
    else:
        i = 0
        first = None
        last = None
        while i < len(inputString):
            if inputString[i] == '(':
                first = i
            if inputString[i] == ')':
                last = i
            if first is not None and last is not None:
                a = inputString[:first]
                b = inputString[last - 1:first:-1]
                if (len(inputString) - 1 > last):
                    c = inputString[last + 1:]
                else:
                    c = ''
                inputString = a + b + c
                first = None
                last = None
                
            i += 1
        return reverseInParentheses(inputString)
