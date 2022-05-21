import pytesseract
from PIL import Image
from numpy.core.defchararray import upper
from pdf2image import convert_from_path
import enchant
# from invoice2data import extract_data
import cv2

# def is_number(in_str):
#     try:
#         _ = float(in_str)
#         return True
#     except Exception as e:
#         return False
#
# def is_decimal(i_num):
#     if round(i_num) != i_num:
#         return True
#     else:
#         return False
#


from PIL import Image
import numpy as np


def read_image(img: object) -> object:
    img = cv2.resize(img, None, fx=1.1, fy=1.1, interpolation=cv2.INTER_CUBIC)
    kernel = np.ones((1, 1), np.uint64)
    img = cv2.dilate(img, kernel, iterations=5)
    img = cv2.erode(img, kernel, iterations=5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.medianBlur(gray, 3)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # OCR
    data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    split_data = data.split(' ')
    dollar_sign_order_enforced = ''
    should_have_dollar_sign = False
    dollar_values = []
    subtotal = 0
    next_entry_is_subtotal = False
    for i in split_data:
        print(i, "\n")
        # every other entry should contain dollar sign

        # if entry contains "subtotal" break off "subtotal" and push into dollar_sign_order_enforced at the next entry
        if has_dollar_sign(i):
            # print("has dollar", i)
            if should_have_dollar_sign is True:
                dollar_values.append(find_price(i))
                dollar_sign_order_enforced += i + ' '
                should_have_dollar_sign = False
        else:
            # print("has no dollar", i)
            if should_have_dollar_sign is False:
                dollar_sign_order_enforced += i + ' '
                should_have_dollar_sign = True

    for i in dollar_sign_order_enforced.split(' '):
        if 'subtotal' in i.lower():
            next_entry_is_subtotal = True
        elif next_entry_is_subtotal:
            next_entry_is_subtotal = False
            subtotal = int(find_price(i))
    return dollar_values, subtotal


def has_dollar_sign(test_string: str):
    for i in test_string:
        if i == '$':
            return True
    return False


def find_price(test_string: str):
    return_string = ''
    for i in test_string:
        if i.isdigit():
            return_string += i
        if i == '.':
            break
    return int(return_string)
