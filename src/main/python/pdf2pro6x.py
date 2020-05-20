import argparse
import io
import os
from uuid import uuid4
from xml.etree import ElementTree
from zipfile import ZipFile

from pdf2image import convert_from_path

from templates import SLIDE, PRESENTATION


def generate_uuid():
    return str(uuid4())


def get_filename_from_path(path):
    return os.path.split(path)[-1]


def get_name_from_path(path):
    return '.'.join(get_filename_from_path(path).split('.')[:-1])


def change_extension(filename, extension):
    return '.'.join(filename.split('.')[:-1]) + '.' + extension


def get_image_filename(name, index):
    return name + '-' + str(index + 1) + '.png'


def create_image_buffers(path_to_pdf, poppler_path=None):
    images = convert_from_path(path_to_pdf, size=(1920, 1080), poppler_path=poppler_path)
    image_buffers = []
    for index, image in enumerate(images):
        image_buffer = io.BytesIO()
        image.save(image_buffer, 'PNG')
        image_buffers.append(image_buffer)

    return image_buffers


def create_pro6_buffer(name, number_images):
    presentation = ElementTree.fromstring(PRESENTATION)
    presentation.find(".//RVSlideGrouping").set('uuid', generate_uuid())
    slides = presentation.find(".//array[@rvXMLIvarName='slides']")

    for index in range(number_images):
        display_slide = ElementTree.fromstring(SLIDE)
        display_slide.set('UUID', generate_uuid())
        image_element = display_slide.find('.//RVImageElement')
        image_element.set('UUID', generate_uuid())
        image_element.set('source', get_image_filename(name, index))
        slides.append(display_slide)

    file_buffer = io.BytesIO()
    ElementTree.ElementTree(presentation).write(file_buffer, encoding='UTF-8', xml_declaration=True)
    return file_buffer


def create_pro6x_file(path_to_pro6x, name, image_buffers, pro6_buffer):
    zip_file = ZipFile(path_to_pro6x, 'w')
    subdir = get_name_from_path(path_to_pro6x)

    for index, buffer in enumerate(image_buffers):
        zip_file.writestr(os.path.join(subdir, 'media', get_image_filename(name, index)), buffer.getvalue())

    zip_file.writestr(os.path.join(subdir, name + '.pro6'), pro6_buffer.getvalue())
    zip_file.close()


def main(path_to_pdf, path_to_pro6x=None, poppler_path=None):
    if not path_to_pro6x:
        path_to_pro6x = change_extension(path_to_pdf, 'pro6x')
    name = get_name_from_path(path_to_pdf)
    image_buffers = create_image_buffers(path_to_pdf, poppler_path)
    pro6_buffer = create_pro6_buffer(name, len(image_buffers))
    create_pro6x_file(path_to_pro6x, name, image_buffers, pro6_buffer)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('path_to_pdf')
    args = arg_parser.parse_args()

    main(args.path_to_pdf)
