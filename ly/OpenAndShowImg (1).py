import cv2

lena = cv2.imread('lena.bmp', cv2.IMREAD_UNCHANGED)
print(lena)
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(lena, "liang", (0, 100), font, 2, (255, 255, 255), 7)

# 显示
cv2.imshow("demo", lena)
key = cv2.waitKey()

# 关闭
cv2.destroyAllWindows()

# 保存
cv2.imwrite('result.bmp', lena)
