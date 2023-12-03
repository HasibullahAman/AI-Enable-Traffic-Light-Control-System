## <div align="center">AI Enabled Traffic lights Control System</div>



## <div align="center">Documentation</div>

See below for a quickstart installation and usage example, and see the [YOLOv8 Docs](https://docs.ultralytics.com) for full documentation on training, validation, prediction and deployment.

<details open>
<summary>Install</summary>

Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI version](https://badge.fury.io/py/ultralytics.svg)](https://badge.fury.io/py/ultralytics) [![Downloads](https://static.pepy.tech/badge/ultralytics)](https://pepy.tech/project/ultralytics)

```bash
pip install ultralytics
pip install pygame

```
### Ardiuno:
1. [Download the latest release](https://downloads.arduino.cc/arduino-ide/arduino-ide_latest_Linux_64bit.AppImage?_gl=1*1wvumxl*_ga*MTU0NDE3Njc0NS4xNzAwNjM4MjIw*_ga_NEXN8H46L5*MTcwMTU4NTMzMy4zLjEuMTcwMTU4NTM5Ny4wLjAuMA..*_fplc*WjUxMzdWbHdEN3lrQmRpdTBwQ1l6STA1aVBaNUg2U3lUekVjMGVBSTZxMVdtcmMzTmhucWV6VmlnemhrZW9mYkhsanBGdk9Ed3lueUJkaVM0dmZIUkdtNzdXTHRBZVZGSFQ2UU5tS04lMkJEbWElMkJqMGRVMyUyRnhGanlrOVkxejl3JTNEJTNE) (The download will start after you click this link. Check your browser’s download manager or the Downloads folder on your computer to find the downloaded file)
2. Double-click the executable (.exe) file.
3. Follow the instructions in the installation guide.
4. When completing the setup, leave Run Arduino IDE ticked to launch the application, or launch it later from the Start Menu.

For alternative installation methods including [Conda](https://anaconda.org/conda-forge/ultralytics), [Docker](https://hub.docker.com/r/ultralytics/ultralytics), and Git, please refer to the [Quickstart Guide](https://docs.ultralytics.com/quickstart).

</details>

<details open>
<summary>Usage</summary>

#### Python

YOLOv8 may also be used directly in a Python environment, and accepts the same [arguments](https://docs.ultralytics.com/usage/cfg/) as in the CLI example above:

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8x.yaml")  # build a new model from scratch
model = YOLO("yolov8x.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="data.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
```

See YOLOv8 [Python Docs](https://docs.ultralytics.com/usage/python) for more examples.

</details>

## <div align="center">Models</div>

YOLOv8 [Detect](https://docs.ultralytics.com/tasks/detect) model trained on the [Car Detection](https://www.kaggle.com/datasets/hasibullahaman/objectdetectiondatasetcar) dataset are available here, as well as YOLOv8 [Classify](https://docs.ultralytics.com/tasks/classify) models pretrained on the [ImageNet](https://docs.ultralytics.com/datasets/classify/imagenet) dataset. [Track](https://docs.ultralytics.com/modes/track) mode is available for all Detect, Segment and Pose models.

<img width="1024" src="https://raw.githubusercontent.com/ultralytics/assets/main/im/banner-tasks.png" alt="Ultralytics YOLO supported tasks">

All [Models](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models) download automatically from the latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on first use.


