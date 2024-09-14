def karatsuba_poly_mult(A, B):
    n = len(A)
    
    if n == 1:
        return [A[0] * B[0]]
    half = n // 2
    A0 = A[:half]
    A1 = A[half:]
    B0 = B[:half]
    B1 = B[half:]
    
    P0 = karatsuba_poly_mult(A0, B0)
    P1 = karatsuba_poly_mult(A1, B1)

    A0A1 = [A0[i] + A1[i] for i in range(half)]
    B0B1 = [B0[i] + B1[i] for i in range(half)]
    
    P2 = karatsuba_poly_mult(A0A1, B0B1)

    result = [0] * (2 * n - 1)

    for i in range(len(P0)):
        result[i] += P0[i]
    
    for i in range(len(P2)):
        result[i + half] += P2[i] - P0[i] - P1[i]
    
    for i in range(len(P1)):
        result[i + 2 * half] += P1[i]
    
    return result

def pad_to_power_of_two(A, B):
    n = 1
    while n < max(len(A), len(B)):
        n *= 2
    A.extend([0] * (n - len(A)))
    B.extend([0] * (n - len(B)))
    return A, B

if __name__ == '__main__':
    A = [9, -10, 7, 6]   
    B = [-5, 4, 0, -2]   

    A, B = pad_to_power_of_two(A, B)

    result = karatsuba_poly_mult(A, B)
    print(result)  