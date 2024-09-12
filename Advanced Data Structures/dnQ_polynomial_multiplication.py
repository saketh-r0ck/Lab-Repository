def karatsuba_poly_mult(A, B):
    n = len(A)
    
    if n == 1:
        return [A[0] * B[0]]
    
    # Split the polynomials into two halves
    half = n // 2
    A0 = A[:half]
    A1 = A[half:]
    B0 = B[:half]
    B1 = B[half:]
    
    # Recursively compute three products
    P0 = karatsuba_poly_mult(A0, B0)
    P1 = karatsuba_poly_mult(A1, B1)
    
    # A0 + A1 and B0 + B1
    A0A1 = [A0[i] + A1[i] for i in range(half)]
    B0B1 = [B0[i] + B1[i] for i in range(half)]
    
    P2 = karatsuba_poly_mult(A0A1, B0B1)
    
    # Combine the results
    result = [0] * (2 * n - 1)
    
    # P0 -> the low order terms (no shift)
    for i in range(len(P0)):
        result[i] += P0[i]
    
    # P2 - P0 - P1 -> the middle order terms (shifted by half)
    for i in range(len(P2)):
        result[i + half] += P2[i] - P0[i] - P1[i]
    
    # P1 -> the high order terms (shifted by n)
    for i in range(len(P1)):
        result[i + 2 * half] += P1[i]
    
    return result

# Ensure polynomials have a length that is a power of 2
def pad_to_power_of_two(A, B):
    n = 1
    while n < max(len(A), len(B)):
        n *= 2
    A.extend([0] * (n - len(A)))
    B.extend([0] * (n - len(B)))
    return A, B

if __name__ == '__main__':
    # Example: Multiply two polynomials
    A = [9, -10, 7, 6]   # Corresponds to 9 - 10x + 7x^2 + 6x^3
    B = [-5, 4, 0, -2]   # Corresponds to -5 + 4x - 2x^3

    # Pad the polynomials so that their lengths are powers of two
    A, B = pad_to_power_of_two(A, B)

    result = karatsuba_poly_mult(A, B)
    print(result)  # Prints the coefficients of the resulting polynomial
