import argparse
import os
from zipfile import ZipFile


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('zip_file')
    arg_parser.add_argument('folder')
    args = arg_parser.parse_args()

    zip_file = ZipFile(args.zip_file, 'w')
    for root, dirs, files in os.walk(args.folder):
        for file in files:
            file = os.path.join(root, file)
            zip_file.write(file, file.replace(args.folder, ''))
    zip_file.close()
