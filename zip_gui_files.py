import argparse
from zipfile import ZipFile

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('zip_file')
    arg_parser.add_argument('contents', nargs="*")
    args = arg_parser.parse_args()

    zip_file = ZipFile(args.zip_file, 'w')
    for content in args.contents:
        zip_file.write(content, content.replace('dist/pdf2pro6x_gui/', ''))
    zip_file.close()
