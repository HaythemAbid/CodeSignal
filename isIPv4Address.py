def solution(inputString):
    digits = inputString.split('.')
    if len(digits) != 4: return False
    for d in digits:
        if not d.isnumeric() or len(d)>3 or int(d)>255 or int(d)<0 or (d.startswith('0') and len(d)>1):
            return False
    return True
