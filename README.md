# yolov5
Exercise yolov5 using taekwon data sample in AIHub


## Prepare data
[taekwon data](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71259)

## Prerequisite
```python
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

## YOLOv5
[yolov5](https://github.com/ultralytics/yolov5)

## Preprocessing
I got ordered only use male samples. 

So extract them from raw samples.
[Extract male](https://github.com/bert13069598/yolov5/blob/ba4a762e29d7afad63ebd6fb4b06b71d029b98e5/count.py#L7)
##

### Reference
[Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

### Adapt label files
[Change json to txt](https://github.com/bert13069598/yolov5/blob/ba4a762e29d7afad63ebd6fb4b06b71d029b98e5/count.py#L45)

### Adapt img files
[Resize size to 640x640](https://github.com/bert13069598/yolov5/blob/ba4a762e29d7afad63ebd6fb4b06b71d029b98e5/count.py#L66)

### Train & Validation & Test
[Split label&img](https://github.com/bert13069598/yolov5/blob/ba4a762e29d7afad63ebd6fb4b06b71d029b98e5/count.py#L86)

## Train
```python
python train.py --img 640 --batch 16 --epochs 3 --data taekwon.yaml --weights yolov5s.pt
```

## Run
