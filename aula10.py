D = np.array([[0,0,0],[0,0,0],[0,0,0]])
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            D[i,j] += (A[i,j]*C[j,i])
           
D        
