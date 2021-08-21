# 使用Python文件读写的方式对位图文件头进行读写

import struct

import numpy as np

import cv2


class PyBMP:

    bmFileSize = 0 # 文件大小

    bmDataOff = 0 # 数据偏移



    bmBpp = 0 # 位深

    bmImgSize = 0 # 位图数据大小

    bmWidth = 0

    bmHeight = 0



    bmData = []



    def loadBmpFile(self, filePath):

        bmpFile = open( filePath, mode='rb')

        # 首先读取文件头

        labelB = bmpFile.read(1)

        labelM = bmpFile.read(1)

        #print( labelB+labelM )



        self.bmFileSize = struct.unpack('I', bmpFile.read(4))[0]

        #print( self.bmFileSize )



        bmpFile.read(4) # 两个保留字bmpFile.read(4)



        self.bmDataOff = struct.unpack('I', bmpFile.read(4))[0]

        #print( self.bmDataOff )



        # 然后读取信息头

        bmpFile.read(4) # 信息头大小



        self.bmWidth = struct.unpack('I', bmpFile.read(4))[0]

        #print( self.bmWidth )



        self.bmHeight = struct.unpack('I', bmpFile.read(4))[0]

        #print( self.bmHeight )



        bmpFile.read(2) # 颜色平面数bmpFile.read(4)



        self.bmBpp = struct.unpack('H', bmpFile.read(2))[0]

        #print( self.bmBpp )



        bmpFile.read(4) # 压缩类型



        self.bmImgSize = struct.unpack('I', bmpFile.read(4))[0]

        if self.bmImgSize == 0:

            self.bmImgSize = int(self.bmWidth * self.bmHeight * (self.bmBpp / 8))

        #print( self.bmImgSize )



        bmpFile.read(16) # 水平分辨率 垂直分辨率 颜色索引数 颜色重要程度bmpFile.read(4)



        # 读取调色板

        bmpFile.read(self.bmDataOff - 54)



        # 读取数据

        self.bmData = struct.unpack('>{}B'.format(self.bmImgSize), bmpFile.read( self.bmImgSize ) )

        self.bmData = np.reshape( self.bmData, (self.bmWidth, self.bmHeight ), )

        self.bmData = self.bmData.astype('uint8')



        bmpFile.close()



    def showBmpInfo(self):

        print('文件大小为{}'.format(self.bmFileSize))

        print('位深为{}'.format(self.bmBpp))

        print('宽度为{}'.format(self.bmWidth))

        print('高度为{}'.format(self.bmHeight))

        print('图像大小为{}'.format(self.bmImgSize))



    def showBmp(self):



        # 显示

        cv2.imshow("demo", self.bmData)

        key = cv2.waitKey()



        # 关闭

        cv2.destroyAllWindows()



test = PyBMP()

test.loadBmpFile('lena.bmp')

test.showBmpInfo()

test.showBmp()