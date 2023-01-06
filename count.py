import os
import json
import shutil
from PIL import Image


def fileCountandSplit():
    metarawpath = '/home/ubuntu/working/hw1/dataset/라벨링데이터/TL2/뒷굽이하고 바깥막기'
    imgrawpath = '/home/ubuntu/working/hw1/dataset/원천데이터/TS1/뒷굽이하고 바깥막기'

    metapath = '/home/ubuntu/working/hw1/pp_dataset/meta'
    imgpath = '/home/ubuntu/working/hw1/pp_dataset/img'

    filelist = os.listdir(metarawpath)
    filecount = 0
    mancount = 0
    womancount = 0

    for filepack in filelist:
        print(filepack)
        remetapath = metarawpath + '/' + filepack
        reimgpath = imgrawpath + '/' + filepack
        filecount += len(os.listdir(remetapath))
        print('파일 수 : ', len(os.listdir(remetapath)))
        files = os.listdir(remetapath)
        for file in files:
            json_file = open(remetapath + '/' + file)
            data = json.load(json_file)
            sex = data.get('labelingInfo')[5].get('actors').get('sex')
            img = data.get('labelingInfo')[3].get('images').get('id')
            if '남자' == sex:
                # json 복사
                shutil.copyfile(remetapath + '/' + file, metapath + '/' + file)
                # img 복사
                shutil.copyfile(reimgpath + '/' + img, imgpath + '/' + img)
                mancount += 1
            elif '여자' == sex:
                womancount += 1

    print('파일 수 : ', filecount)
    print('남자 수 : ', mancount)
    print('여자 수 : ', womancount)


def label(metapath, totalpath, file):
    # file = 'B-017-A035-M-B2006-S-20211109-01-01-E01.json'
    json_file = open(metapath + file)
    data = json.load(json_file)

    box = data.get('labelingInfo')[1].get('box').get('boundingBox')
    Xmin = box.get('Xmin')
    Xmax = box.get('Xmax')
    Ymin = box.get('Ymin')
    Ymax = box.get('Ymax')

    Xcen = (Xmin + Xmax) / 2 / 1920
    Ycen = (Ymin + Ymax) / 2 / 1080
    w = (Xmax - Xmin) / 1920
    h = (Ymax - Ymin) / 1080

    line = '0', ' ', str(Xcen), ' ', str(Ycen), ' ', str(w), ' ', str(h)
    with open(totalpath + file.replace('json', 'txt'), 'w', encoding='UTF-8') as f:
        f.writelines(line)


def ImgResize(imgpath, totalpath, file):
    # file = 'B-017-A035-M-B2006-S-20211109-01-01-E01.jpg'
    img = Image.open(imgpath + file)
    img_resize = img.resize((640, 640))
    img_resize.save(totalpath + file)


imgpath = '/home/ubuntu/working/hw1/pp_dataset/img/'
metapath = '/home/ubuntu/working/hw1/pp_dataset/meta/'
totalpath = '/home/ubuntu/working/hw1/pp_dataset/image/'

finalpath = '/home/ubuntu/working/hw1/pp_dataset/taekwon/'


# imglist = os.listdir(imgpath)
# metalist = os.listdir(metapath)
# for img, meta in zip(imglist, metalist):
#     ImgResize(imgpath, totalpath, img)
#     label(metapath, totalpath, meta)

def TrainValSplit():
    op = 'images/'
    totalpath = f'/home/ubuntu/working/hw1/pp_dataset/{op}'
    totalL = len(os.listdir(totalpath))
    trainL = int(totalL * 0.8)
    valL = int(totalL * 0.1)
    testL = totalL - trainL - valL

    print('total :', totalL, 'train :', trainL, 'val :', valL, 'test :', testL)

    for i, file in zip(range(0, totalL), os.listdir(totalpath)):
        if i < trainL:
            shutil.copyfile(totalpath + file, finalpath + f'train/{op}' + file)
        elif trainL <= i < trainL + valL:
            shutil.copyfile(totalpath + file, finalpath + f'val/{op}' + file)
        elif trainL + valL <= i < totalL:
            shutil.copyfile(totalpath + file, finalpath + f'test/{op}' + file)


TrainValSplit()
