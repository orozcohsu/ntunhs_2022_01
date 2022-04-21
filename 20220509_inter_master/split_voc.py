import os
import random

trainval_percent = 0.8                          # 訓練集+驗證集總占比
train_percent = 0.875                           # 訓練集在trainval_percent裏的train占比，0.875*0.8=0.7，因此訓練集在總樣本中占比70%
VOCdevkit_path = 'VOCdevkit'                    # 數據集文件路徑
random.seed(0)                                  # 設定種子，使得程序能够複現

print("Generate txt in ImageSets.")
xmlfilepath = os.path.join(VOCdevkit_path, 'VOC2007/Annotations')           # 標簽文件路徑
saveBasePath = os.path.join(VOCdevkit_path, 'VOC2007/ImageSets/Main')       # 訓練集、驗證集、測試集txt文件的所在路徑
temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num = len(total_xml)                            # 獲得數據集樣本的總數量
list = range(num)                               # 獲得數據集樣本的索引
tv = int(num * trainval_percent)                # 驗證集+訓練集樣本的總數量
tr = int(tv * train_percent)                    # 訓練集樣本的數量
trainval = random.sample(list, tv)              # 訓練集+驗證集樣本索引構成的列錶
train = random.sample(trainval, tr)             # 訓練集樣本索引構成的列錶
# random.sample(list, tv) 錶示從list中生成一個長度為tv新列錶，新列錶中的元素從list中取樣獲得
# 而list是一個range對象，錶示數據集的索引

print("train and val size", tv)
print("train size", tr)

ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'  # total_xml[i][:-4]之所以只到-4，是因為最後4比特是 .xml，這個我們暫時不需要
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
print("Generate txt in ImageSets done.")

