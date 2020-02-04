def connected(img, i, j):
    
    x = [img[i-1][j-1], img[i][j-1], img[i+1][j-1]]
    y = [img[i-1][j+1], img[i][j+1], img[i+1][j+1]]
    m = img[i-1][j-1:j+2]
    n = img[i+1][j-1:j+2]
    
    a = any(x) and any(y)
    b = any(m) and any(n)
    
    if(a or b):
        return True
    else:
        return False

def bridging(img):
    aux = np.array(img)
    
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            
            if(img[i][j]==0):
                if(connected(img, i, j)):
                    aux[i][j] = 1
            
    return aux