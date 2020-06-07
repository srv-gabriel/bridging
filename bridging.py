def connected4(img, i, j):
    l = [img[i-1][j], img[i][j+1], img[i+1][j], img[i][j-1]]
    
    if(sum(l)>1):
        return True
    else:
        return False

def bridging(img):
    aux = np.array(img)
    
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            
            if(img[i][j]==0):
                if(connected4(img, i, j)):
                    aux[i][j] = 1
            
    return aux
