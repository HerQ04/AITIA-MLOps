import argparse
import roboflow
from roboflow import Roboflow

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yoloversion', type=int, default=5, help='YOLO version to be used')
    parser.add_argument('--workspace', type=str, default='msc-onlab-1', help='the Roboflow workspace containing the project')
    parser.add_argument('--project', type=str, default='person-so5ko', help='the id of the Roboflow project')
    parser.add_argument('--version', type=int, default=1, help='the version of the dataset')
    parser.add_argument('--api_key', type=str, default='FYXm4j188EfCcP2ODqYO', help='API key')  #This key is not valid
    parser.add_argument('--create_dataset', action='store_true', help='Flag to create a dataset')
    return parser.parse_args()

def generate_version(workspace="msc-onlab-1", project="person-so5ko", apikey="FYXm4j188EfCcP2ODqYO", width=640, height=640):
    rf = roboflow.Roboflow(api_key=apikey)
    project = rf.workspace(workspace).project(project)
    version=project.generate_version(settings = {
        "augmentation": {},
        "preprocessing": {
            "auto-orient": True,
            "resize": { "width": width, "height": height, "format": "Stretch to" },  # Set width and height to 0 to disable resizing
        }
    })
    return version
    
def download_dataset(workspace="msc-onlab-1", project="person-so5ko", apikey="FYXm4j188EfCcP2ODqYO", version=4, yoloversion=5):
    rf = roboflow.Roboflow(api_key=apikey)
    project = rf.workspace(workspace).project(project)
    dataset = project.version(version).download(f"yolov{yoloversion}")
    return dataset.location



if __name__ == '__main__':
    opt = parse_opt()
    vers=opt.version
    if(opt.create_dataset):
        vers=generate_version(opt.workspace, opt.project, opt.api_key, width=640, height=640)
    
    ds_location = download_dataset(opt.workspace, opt.project, opt.api_key, vers, opt.yoloversion)
    print(f"Roboflow project dataset downloaded to {ds_location}")
