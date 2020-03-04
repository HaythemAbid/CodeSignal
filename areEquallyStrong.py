def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = [yourLeft, yourRight]
    friend = [friendsRight, friendsLeft]
    stronger = []
    for i in you:
        if i not in friend:
            stronger.append(i)
    if (len(stronger) > 0):
        return False
    else:
        return True
