import numpy as np
def inverse_matrix(c1,c2,b):

    mat = np.array([c1,c2])
    inverse = np.linalg.inv(mat)
    return np.dot(inverse,b)

if __name__ == "__main__":
    
    p1 = 0
    p2 = 0
    z_coeff = [4500,5000]

    c1 = [5000,4000]
    c2 = [400,500]
    c3 = [0,1]
    c4 = [1,0]
       
    b = [6000,600,1,1,0,0]

    points = []
    points.append(inverse_matrix(c1,c2,[b[0],b[1]]))
    points.append(inverse_matrix(c1,c4,[b[0],b[3]]))
    points.append(inverse_matrix(c2,c3,[b[1],b[2]]))
    points.append(inverse_matrix(c3,c4,[b[2],b[4]]))
    points.append(inverse_matrix(c4,c3,[b[3],b[5]]))

    z = 0
    optimal_point = []
    for x,y in points:
        total = 4500*x + 5000*y
        if z <= total:
            optimal_point = [x,y]
            z = total

    print("Optimal partitions : ",optimal_point)
    print("Maximum profit :", z)