"""
Resize images.
"""

import argparse
import os
import sys

import cv2


def bicubic(img, magnification):
    """
    Resize images by bicubic.

    Parameters
    ----------
    img: numpy.ndarray
        Image to be resezed.
    magnification: float
        Magnification.

    Returns
    -------
    dst: numpy.ndarray
        Resezed image.
    """

    height, width = map(
        int, [img.shape[1]*magnification, img.shape[0]*magnification])
    dst = cv2.resize(
        img, (height, width), interpolation=cv2.INTER_CUBIC)

    return dst


def main():
    """
    Entry point.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory that has images.')
    parser.add_argument('--magnification', '-m', type=float, default=0.5,
                        help='Magnification.')
    args = parser.parse_args()

    path = args.dir
    magnification = args.magnification
    magnification_inverse = int(1 / magnification)
    assert os.path.isdir(path)

    imgs = [os.path.join(path, file_) for file_ in os.listdir(path)
            if os.path.splitext(file_)[-1] in ['.png', '.jpg']]

    for img_path in imgs:
        root, ext = os.path.splitext(img_path)
        save_path = f'{root}x{magnification_inverse}{ext}'

        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        dst = bicubic(img, magnification)
        cv2.imwrite(save_path, dst)


if __name__ == '__main__':
    main()
