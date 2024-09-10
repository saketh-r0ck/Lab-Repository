from math import sin,cos,pi
def FFT(a,inverse_flag):
    n = len(a)
    if n==1 :
        return a
    a_e ,a_o = a[::2] , a[1::2]
    y_e , y_o = FFT(a_e,0) , FFT(a_o,0)

    if inverse_flag:
        theta = -2*pi/n 
    else:
        theta = 2*pi/n

    w = list(complex(cos(theta*i), sin(theta*i)) for i in range(n)) 
    y = [0]*n
    half = n//2
    for k in range(half):
        y[k] = y_e[k] + w[k] * y_o[k]
        y[k + half] = y_e[k] - w[k] * y_o[k]

    if inverse_flag: 
        return [val/n for val in y]
    else:    
        return y

if __name__ == '__main__':
    a = [1,2,3,4]
    b = FFT(a,0)
    c = FFT(b,1)
    print(c)
    print(b)