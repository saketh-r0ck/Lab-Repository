
def first_fit(wwight,n,c):
    res = 0
    bags = [0]*n
    for w in weight:
        j = 0
        while j<res :
            if bags[j] >= w :
                bags[j] -= w
                break
            j += 1

        if j==res :
            bags[res] = c - w
            res += 1
    return res
if __name__ == "__main__":
    weight = [0.5,0.7,0.5,0.2,0.4,0.2,0.5,0.1,0.6]
    capacity = 1
    n = len(weight)
    x = first_fit(weight,n,capacity)
    print("No of bags required :",x)