from math import sin, cos, pi
import numpy as np

def bit_reverse_copy(a):
    n = len(a)
    result = [0] * n
    log_n = int(np.log2(n))
    
    for k in range(n):
        rev_k = int('{:0{width}b}'.format(k, width=log_n)[::-1], 2)
        result[rev_k] = a[k]
    
    return result

def iterative_fft(a, inverse_flag):
    n = len(a)
    A = bit_reverse_copy(a)
    
    theta = (2 * pi / n) * (-1 if inverse_flag else 1)
    wn = [complex(cos(theta * i), sin(theta * i)) for i in range(n)]
    
    half_size = 1
    while half_size < n:
        step_size = half_size * 2
        for i in range(0, n, step_size):
            for k in range(half_size):
                w = wn[(k * n) // step_size]
                u = A[i + k]
                v = w * A[i + k + half_size]
                A[i + k] = u + v
                A[i + k + half_size] = u - v
        half_size *= 2
    
    if inverse_flag:
        return [x / n for x in A]
    else:
        return A

def polynomial_multiplication(a1, a2):
    n = 1
    while n < len(a1) + len(a2) - 1:
        n *= 2
    
    a1.extend([0] * (n - len(a1)))
    a2.extend([0] * (n - len(a2)))
    
    fft_a1 = iterative_fft(a1, 0)
    fft_a2 = iterative_fft(a2, 0)
    
    pointwise_mul = np.multiply(fft_a1, fft_a2)    
    result = iterative_fft(pointwise_mul, 1)
    
    result = [round(x.real) for x in result]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return result

if __name__ == '__main__':
    a1 = [9, -10, 7, 6]
    a2 = [-5, 4, 0, -2]
    print(polynomial_multiplication(a1, a2))
