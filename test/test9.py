# 卷积操作
def matrix_conv(arr,kernel):
    n = len(kernel)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += arr[i,j]*float(kernel[i,j])
    return ans

def conv2d(img,kernel):
    n = len(lernel)
    img1 = np.zeros((img.shape[0]+2*(n-1),img.shape[1]+2*(n-1)))
    img1 [(n-1):(n+img.shape[0]-1),(n-1):(n+img.shape[1]-1)] = img
    img2 = np.zeros((img1.shape[0]-n+1,img1.shape[1]-n+1))
    for i in range(img1.shape[0]-n+1):
        for j in range(img1.shape[1]-n+1):
            temp = img1[i:i+n:j+n]
            img2[i,j] = matrix_conv(temp,kernel)
    new_img = img2[(n-1):(n+img.shape[0]-1),(n-1):(n+img.shape[1]-1)]
    return new_img