# CONVERT JPG TO PNG

import cv2
# src = cv2.imread("C://Users/Guo/Desktop/OneInch.jpg",1)

# 转为jpg 
# 第三个参数0-100可选，值越大，图片质量越高
# cv2.imwrite("C://Users//Guo//Desktop//save10.jpg",src,[int(cv2.IMWRITE_JPEG_QUALITY),10])
# cv2.imwrite("C://Users//Guo//Desktop//save100.jpg",src,[int(cv2.IMWRITE_JPEG_QUALITY),100])

# 转为png
# 从0-9.较高的值意味着更小的size和更长的压缩时间  而默认值是3
jpg_path = "C:/Users/Guo/Desktop/0038/rgb/"
jpg_names = os.listdir(jpg_path)
# os.mkdir("C:/Users/Guo/Desktop/0038/png")

png_path = "C:/Users/Guo/Desktop/0038/png/"

for jpg_name in jpg_names:
    splited = jpg_name.split('.')[0]
    splited = splited+'.png'
    src = cv2.imread(os.path.join(jpg_path,jpg_name))
    cv2.imwrite(os.path.join(png_path,splited),src, [int(cv2.IMWRITE_PNG_COMPRESSION), 6])
