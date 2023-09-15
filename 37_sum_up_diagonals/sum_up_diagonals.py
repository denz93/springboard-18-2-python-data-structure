def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    def diagonal(size, ring):
        if size < 1:
            return 0
        if size == 1:
            return matrix[ring][ring] * 2
        if size == 2:
            return matrix[ring][ring] + matrix[ring+1][ring+1] + matrix[ring][ring+1] + matrix[ring+1][ring]
        outter = matrix[ring][ring] + matrix[ring+size-1][ring+size-1] + matrix[ring][ring+size-1] + matrix[ring+size-1][ring]
        return diagonal(size-2, ring+1) + outter
    return diagonal(len(matrix), 0)