import torch
import yaml
import os
import sys
import argparse
import webbrowser
import time
import shutil

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yolov8', action='store_true', help='the flag for using YOLOv8')
    parser.add_argument('--img', type=int, default=640, help='train, val image size (pixels)')
    parser.add_argument('--batch', type=int, default=-1, help='total batch size for all GPUs, use -1 for autobatch')
    parser.add_argument('--epochs', type=int, default=100, help='total training epochs')
    parser.add_argument('--model', type=str, default='yolov5m', help='model to be used for training')
    parser.add_argument('--name', default='exp', help='name of the current project output')
    parser.add_argument('--dataset_name', help='dataset name')
    parser.add_argument('--outputdir', type=str, default='C:/yolov5', help='the folder where the result of the training inside the runs/train folder shall be saved')
    parser.add_argument('--workspace', type=str, default='msc-onlab-1', help='the Roboflow workspace containing the project')
    parser.add_argument('--project', type=str, default='person-so5ko', help='the id of the Roboflow project')
    parser.add_argument('--version', type=int, default=4, help='the version of the dataset')
    parser.add_argument('--YOLOv5_path', type=str, help='path for YOLOv5') 
    return parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt()

    if not os.path.isdir(opt.YOLOv5_path):
        raise FileNotFoundError("YOLOv5_path is not valid")  

    sys.path.append(opt.YOLOv5_path) 
    try:
        import train
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Failed to import module 'train'")
    
    
    if not os.path.isdir(f"{opt.YOLOv5_path}/{opt.dataset_name}"):
        raise FileNotFoundError(f"The dataset is not in the YOLOv5 directory: {opt.YOLOv5_path}/{opt.dataset_name}")
    
    
    train.run(img=opt.img, batch=opt.batch, epochs=opt.epochs, data=f"{opt.YOLOv5_path}/{opt.dataset_name}/data.yaml", cfg=f"{opt.YOLOv5_path}/models/{opt.model}.yaml", weights=f"{opt.model}.pt", name=opt.name)


