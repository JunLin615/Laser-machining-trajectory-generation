# -*- coding: utf-8 -*-
"""
@Time:2021/11/2 22:43
@Auth"JunLin615
@File:bjsb.py
@IDE:PyCharm
@Motto:With the wind light cloud light mentality, do insatiable things
@email:ljjjun123@gmail.com 
"""
import cv2
import numpy as np
def conversion(file_name,save_filename):
    #file_name = "D:\北工硕士阶段\竞赛\互联网+\轨迹2.png"
    img = cv2.imdecode(np.fromfile(file_name,dtype=np.uint8),-1)
    #img = cv2.bitwise_not(img)
    gray = img[:,:,0]
    height,width=gray.shape
    dst=np.zeros((height,width,1),np.uint8)
    for i in range(height):
        for j in range(width):
            dst[i,j]=255-gray[i,j]

    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.bitwise_not(img)
    cv2.imshow("source file", img)
    #filename = "D:\\北工硕士阶段\\会议\\main41.png"
    #cv2.imwrite('D:/main41.png', img)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    #filename = "D:\\北工硕士阶段\\会议\\main42.png"
    #cv2.imwrite('D:/北工硕士阶段/会议/main42.png', img)

    cv2.imshow("trajectory", img)

    cv2.waitKey(0)

    import codecs
    #filename2 = "D:\project_file\python\图像处理\条纹骨架\picture\main4.txt"
    #filename2 = filepath +
    f = codecs.open(save_filename, 'w', 'utf-8')

    # f.write(str(list))

    #print(contours)
    contours_a = []
    for a in contours:
        for b in a :
            for c in b :
                contours_a.append(c)

    contours_a = np.vstack((contours_a, contours_a[0]))
    contours_d = np.diff(contours_a.T)
    print(contours_d)
    for i in contours_d.T:
        f.write(str(i[0]) + ',' + str(i[1]) + '\r\n')  # \r\n为换行符

    f.close()