import cv2
import os
import sys

if len(sys.argv) < 3:
    print("no directory specified, please input target directory")
    exit()

root_dir = sys.argv[1]
print("input dir:", root_dir)
output_dir = sys.argv[2]
print("output dir:", output_dir)

if not os.path.exists(root_dir):
    print("cannot find such directory: " + root_dir)
    exit()

if not os.path.exists(output_dir):
    print("cannot find such directory: " + output_dir)
    exit()

crop_size = 640
for filename in os.listdir(root_dir):
    img = cv2.imread(os.path.join(root_dir, filename))
    if img is None:
        print(filename, "image is empty, SKIP!")
        continue
    imgH = img.shape[0]
    imgW = img.shape[1]
    if imgH < crop_size or imgW < crop_size:
        print(filename, "contain resolution lower than", crop_size, "ignore!")
        continue
    if imgW == crop_size and imgW == crop_size:
        print(filename, "already in the desired resolution:", crop_size)
        continue
    offSetX = int((imgW - crop_size)/2)
    img = img[imgH - crop_size:imgH, offSetX:offSetX + crop_size, :]
    cv2.imwrite(os.path.join(root_dir, filename), img)
