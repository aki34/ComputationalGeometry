import numpy as np

def LeftofDirectedLine(p, q, r):
    if np.cross((q-p), (r-p)) > 0:
        return True
    else:
        return False


def clockwisesort(E):
    L=[]
    L.extend(list(E[0]))
    E = np.delete(E,obj=0,axis=0)
    while E.size!=0:
        for i in range(E.shape[0]):
            if E[i,0] == L[-1]:
                L.append(E[i,1])
                E = np.delete(E,obj=i,axis=0)
                break
    return L


def SlowConvexHull(P):
    '''
    input : A set P of points in plane. (N x 2)
    output : A list containing the vertices of CH(P) in clockwise order. (N x 2)
    '''
    E=[]
    for i in range(P.shape[0]):
        for j in range(P.shape[0]):
            if i == j:
                continue
            valid = True
            for r in range(P.shape[0]):
                if r == i or r == j:
                    continue
                if LeftofDirectedLine(P[i],P[j],P[r]):
                    valid = False
                    break
            if valid:
                E.append((i,j))

    L = clockwisesort(np.array(E))
    return P[L]


def ConvexHull(P):
    #TODO
    pass

if __name__ == "__main__":
    E=np.array(((1,3),(5,8),(9,2),(3,9),(2,5)))
    print(clockwisesort(np.array(E)))