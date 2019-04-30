import numpy as np

def LeftofDirectedLine(p, q, r):
    if np.cross((q - p), (r - p)) > 0:
        return True
    else:
        return False


def clockwisesort(E):
    L = []
    L.extend(list(E[0]))
    E = np.delete(E,obj=0,axis=0)
    while E.size != 0:
        for i in range(E.shape[0]):
            if E[i,0] == L[-1]:
                L.append(E[i,1])
                E = np.delete(E,obj=i,axis=0)
                break
    return L


def NotClockwise(L):
    p,q,r = L[-3:]
    if np.cross((q - p), (r - q)) > 0:
        return True
    else:
        return False

def SlowConvexHull(P):
    '''
    input : A set P of points in plane. (N x 2)
    output : A list containing the vertices of CH(P) in clockwise order. (N x 2)
    '''
    E = []
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

    L = clockwisesort(np.array(E))[:-1]
    return P[L]


def ConvexHull(P):
    '''
    input : A set P of points in plane. (N x 2)
    output : A list containing the vertices of CH(P) in clockwise order. (N x 2)
    '''
    P_sorted = P[np.argsort(P[:,1])] # sort the points by y-coordinate
    P_sorted = P_sorted[np.argsort(P_sorted[:,0])] # sort the points by x-coordinate
    L_upper = P_sorted[:2]
    for i in range(2,P_sorted.shape[0]):
        L_upper = np.concatenate((L_upper, P_sorted[i].reshape(1,2)), axis=0)
        while L_upper.shape[0] >= 3 and NotClockwise(L_upper):
            L_upper = np.delete(L_upper,obj=-2,axis=0)

    L_lower = P_sorted[-1:-3:-1]
    for i in range(P_sorted.shape[0]-2)[::-1]:
        L_lower = np.concatenate((L_lower, P_sorted[i].reshape(1,2)), axis=0)
        while L_lower.shape[0] >= 3 and NotClockwise(L_lower):
            L_lower = np.delete(L_lower,obj=-2,axis=0)

    return np.concatenate((L_upper,L_lower[1:-1]),axis=0)
    

if __name__ == "__main__":
    E = np.array(((1,3),(5,8),(9,2),(3,9),(2,5)))
    print(clockwisesort(np.array(E)))