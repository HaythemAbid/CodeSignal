def solution(a):
    a.reverse()
    k= []
    for n in a:
        k.append(format(n,'08b'))
        print(k)
    result = ''.join(k)
    return int(result,2)
