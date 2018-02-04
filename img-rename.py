import argparse
import exifread
import glob
import os, os.path

parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="The directory to rename files for",
        type=str)
args = parser.parse_args()
if args.dir:
    directory = args.dir
    image_types = ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff']

    for f in os.listdir(directory):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in image_types:
            continue
        else:
            file_path = directory + f
            fl = open(file_path, 'rb')
            tags = exifread.process_file(fl)
            if "Image DateTime" in tags.keys():
                os.rename(file_path, directory + 'img_' + "{}".format(tags["Image DateTime"]).replace(':', '').replace(' ', '_') + ext)
