import json

with open('labels_unlabeled_images.json','r') as f:
    coco = json.load(f)

ann_list = coco['annotations']

for i in range(len(ann_list)):
    bbox = ann_list[i]['bbox']
    x = bbox[0] + bbox[2]
    y = bbox[1] + bbox[3]
    w = bbox[2]
    h = bbox[3]

    new_box = [x,y,w,h]
    seg = [[x,y,x+w,y,x+w,y+h,x,y+h]]
    area = float(w)*float(h)

    coco['annotations'][i]['bbox'] = new_box
    coco['annotations'][i]['segmentation'] = seg
    coco['annotations'][i]['area'] = area

with open('labels_unlabeled_images_modified.json','w') as jsonFile:
    json.dump(coco, jsonFile)