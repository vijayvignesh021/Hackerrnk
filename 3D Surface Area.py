def surfaceArea(A):
    hight = len(A)
    width = len(A[0])
    s = 2*hight* width + A[0][-1] + A[-1][0] + 2*A[-1][-1]
    
    for i in range(0,hight-1):
        s += A[i][0] + A[i][-1]
        for j in range(width):
            s += abs(A[i][j] - A[i+1][j])
    for i in range(width-1):
        s += A[0][i] + A[-1][i]
        for j in range(hight):
            s += abs(A[j][i] -A[j][i+1])
