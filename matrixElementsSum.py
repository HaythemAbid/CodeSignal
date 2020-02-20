def matrixElementsSum(matrix):
    colonne = len(matrix[0])
    echangematrix = [1 for i in range(colonne)]
    sum = 0
    for ligne in matrix:
        for index in range(colonne):
            if echangematrix[index]:
                if ligne[index]:
                    sum += ligne[index]
                else:
                    echangematrix[index] = 0
    return sum
