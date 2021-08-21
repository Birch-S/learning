import cv2



lena = cv2.imread('lena.bmp', cv2.IMREAD_UNCHANGED)

print( lena )



# 显示

cv2.imshow("demo", lena )

key=cv2.waitKey()



# 关闭

cv2.destroyAllWindows()



# 保存

# cv2.imwrite( 'result.bmp', lena )