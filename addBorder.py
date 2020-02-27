def addBorder(picture):
    size = len(picture[0])
    new_picture = []
    border = ('*' * (size + 2))
    new_picture.append(border)
    for i in picture:
        new_picture.append('*' + i + '*')
    new_picture.append(border)
    return new_picture
