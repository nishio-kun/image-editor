"""
This module changes color of images.
"""

import argparse
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np


def change_color(image, _from, _to):
    """
    Change color of an image from specified color to specified color.
    """

    image[np.where((image == _from).all(axis=2))] = _to


def show_image(img):
    """
    Show image using cv2.
    """

    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', img)
    cv2.waitKey() & 0xff
    cv2.destroyAllWindows()


def show_image_array(img):
    """
    Show image using matplotlib.
    """

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    plt.show()


def save_image(path, img):
    """
    Save image.
    """

    cv2.imwrite(path, img)


def main():
    """
    Entry point.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', choices=['show', 'change'],
                        help='"cmd" is "show" or "change".')
    parser.add_argument('img_path', help='Path of the target image.')
    parser.add_argument('-f', type=int, choices=range(0, 256),
                        help='Change color from that.')
    parser.add_argument('-t', type=int, choices=range(0, 256),
                        help='Change color to that.')
    parser.add_argument('-s', '--save', help='Save image.')
    args = parser.parse_args()

    cmd = args.cmd
    img_path = args.img_path
    from_ = args.f
    to = args.t
    save_img_path = args.save

    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    if cmd == 'show':
        show_image_array(img)
    elif cmd == 'change':
        if not all([from_, to]):
            print('"-f", "-t" are required if "cmd" is "change"')
            sys.exit(1)
        change_color(img, from_, to)
        show_image(img)

    if save_img_path:
        save_image(save_img_path, img)
        print(f'saved to {save_img_path}')


if __name__ == '__main__':
    main()
