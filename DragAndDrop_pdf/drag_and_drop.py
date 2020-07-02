#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import sys
import pathlib
import pdf2image

# データ読み込みクラス


class Class_Img_PreProcessing():
    '''
    画像データの前処理をまとめたクラス
    '''

    # def __init__(self,filepath="",cv2img = None):
    #     '''
    #     コンストラクタ (filepath=指定したパス の画像の読み込み,もしくはcv2img=numpy形式データを代入)

    #     '''
    #     if filepath !="" :  #ファイルパスが指定された場合
    #         self.img = cv2.imread(filepath)
    #     elif cv2img != None: #numpy形式データが入力された場合
    #         self.img = cv2img
    #     else:
    #         self,img = None

    # def get_gray_img(self,color_im= "None"):
    #     '''
    #     グレースケール画像を取得する (color_im:カラー画像データ(option))
    #     '''
    #     if color_im is "None":
    #         if self.img is None:
    #             return None
    #         else:
    #             return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    #     else:
    #         return cv2.cvtColor(color_im, cv2.COLOR_BGR2GRAY)

    # def flip_img(self,mode="x"):
    #     '''
    #     画像を反転させる
    #     x: 横方向反転、y:縦方向反転 xy:両方向反転
    #     '''
    #     if self.img is None:
    #         return None
    #     else:
    #         if mode == "x": #X軸方向反転
    #             result = cv2.flip(self.img,1)
    #         elif mode == "y": #Y軸方向反転
    #             result = cv2.flip(self.img,0)
    #         elif mode == "xy": #両方向反転
    #             result = cv2.flip(self.img,-1)
    #         else:
    #             result = self.img
    #     return result

    # def __init__(self, filepath="", cv2img=None):
    #     '''
    #     コンストラクタ (filepath=指定したパス の画像の読み込み,もしくはcv2img=numpy形式データを代入)

    #     '''
    # if filepath != "":  # ファイルパスが指定された場合
    #     self.img = cv2.imread(filepath)
    # elif cv2img != None:  # numpy形式データが入力された場合
    #     self.img = cv2img
    # else:
    #     self, img = None


def __init__(self, filepath="", cv2img=None):
    images = pdf2image.convert_from_path(filepath)
    images.save(pathlib.Path()/'1.png')


#         pdf_files = pathlib.Path('in_pdf').glob('*.pdf')


# img_dir = pathlib.Path('out_img')

# for pdf_file in pdf_files:
#     base = pdf_file.stem
#     images = pdf2image.convert_from_path(pdf_file, grayscale=True, size=640)
#     for index, image in enumerate(images):
#         image.save(img_dir/pathlib.Path(base + '-{}.png'.format(index + 1)),
#                    'png')


if __name__ == '__main__':

    # target_ext = ['.jpeg','.png','.tif']
    target_ext = ['.pdf', 'jpeg1']

    for indx in range(1, len(sys.argv)):
        filename = sys.argv[indx]
        root, ext = os.path.splitext(filename)
        print(ext)
        for indx2 in range(len(target_ext)):
            print(filename)
            images = pdf2image.convert_from_path(filename)
            images.save(pathlib.Path()/'1.png')
            # img_inst = Class_Img_PreProcessing(filename)
            # flip_img = img_inst.flip_img(mode="x")
            # gray_img = img_inst.get_gray_img(color_im=flip_img)
            # cv2.imshow("Windowname", gray_img)
            # cv2.waitKey(0)
