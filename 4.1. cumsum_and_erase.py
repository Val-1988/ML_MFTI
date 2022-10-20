A = [5, 1, 4, 5, 14]
B = []

def cumsum_and_erase(A, erase=1):
    B = [elem for elem in [sum(A[0:i[0]]) for i in enumerate(A, 1)] if not elem == erase]
    return B

print(cumsum_and_erase(A))
