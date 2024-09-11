from math import sin,cos,pi
import numpy as np
def FFT(a,inverse_flag):
	n = len(a)
	if n==1 :
		return a
	a_e ,a_o = a[::2] , a[1::2]
	y_e , y_o = FFT(a_e,inverse_flag) , FFT(a_o,inverse_flag)

	if inverse_flag:	
		theta = -2*np.pi/n 
	else:
		theta = 2*np.pi/n

	w = 1
	wn = np.exp(1j * theta) 
	y = [0]*n

	for k in range(n//2):
		y[k] = y_e[k] + w * y_o[k]
		y[k + n//2] = y_e[k] - w * y_o[k]
		if inverse_flag:
			y[k] /= 2
			y[k + n//2 ] /= 2
		w = w * wn
	return y
        
def polynomial_multiplication(a1,a2):
	n = 1
	while n < len(a1)+len(a2)-1:
		n*=2
	
	a1.extend([0]*(n - len(a1)))
	a2.extend([0]*(n - len(a2)))
	
	b1 = FFT(a1,0)
	b2 = FFT(a2,0)
	
	point_mul = np.multiply(b1,b2)
	
	result = FFT(point_mul,1)
	result = [round(x.real) for x in result]
	while len(result) > 1 and result[-1] == 0:
        	result.pop()
	return result
	

if __name__ == '__main__':
    a1 = [9,-10,7,6]
    a2 = [-5,4,0,-2]
    print(polynomial_multiplication(a1,a2))
    
    
