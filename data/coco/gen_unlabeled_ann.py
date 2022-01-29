import json
import os

files = os.listdir("unlabeled2017")

coco = {}

coco['info'] = {
        "description": "COCO animals Quentin",
        "url": "http://cocodataset.org",
        "version": "1.0",
        "year": 2021,
        "contributor": "Quentin",
        "date_created": "2021/21/12"
    }

coco['licenses'] = [
        {
            "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
            "id": 1,
            "name": "No license"
        }
    ]

coco['images'] = []

for file in files:
    id = file[0].split('.')[0][3:]
    im = {
        "license":1,
        "id":id,
        "filename":file
    }
    coco['images'].append(im)

with open('annotations/image_info_unlabeled2017.json','w') as jsonFile:
    json.dump(coco, jsonFile)