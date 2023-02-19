import os, sys

if len(sys.argv) < 2:
    print("no directory specified, please input target directory")
    exit()

root_dir = sys.argv[1]

files = os.listdir(root_dir)
for file in files:
    new_name = file.split("2d_")[1]
    os.rename(root_dir + file, root_dir + new_name) #image