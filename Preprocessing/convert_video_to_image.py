import cv2

video = cv2.VideoCapture("D:\AI-Enable-Traffic-Light-Control-System-ATL-\Dataset\Video\For Test/City traffic in Bangkok.mp4")
success, image = video.read()

count=0 

delay = 1000

while video.isOpened():
    success, image = video.read()

    if not success:
        break

    video.set(cv2.CAP_PROP_POS_MSEC, (count * delay))

    success, image = video.read()

    if not success:
        break

    cv2.imwrite('./Labeling/Frame/A1%d.png' % count, image)
    count+=1