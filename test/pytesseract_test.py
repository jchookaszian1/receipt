from pytesseract_main import read_image


def test_output_equals_jpg():
    output, subtotal = read_image('../receipt.jpg')
    total_success = 0
    expected_dollars = [49, 49, 12, 10, 42, 17, 5, 184, 21, 206]
    for idx, i in enumerate(output):
        if expected_dollars[idx] == i:
            total_success += 1
    printOutputStats(total_success, expected_dollars, subtotal)
    assert output is expected_dollars


def test_output_equals_jpg1():
    output, subtotal = read_image('../receipt_1.jpg')
    total_success = 0
    expected_dollars = [14, 14, 28, 7, 16, 4, 18, 46, 17, 164, 19, 6, 189]
    for idx, i in enumerate(output):
        if expected_dollars[idx] == i:
            total_success += 1
    printOutputStats(total_success, expected_dollars, subtotal)
    assert output is expected_dollars


def printOutputStats(total_success, expected_dollars, subtotal):
    print('SUCCESS RATE: ', "{0:.0%}".format((total_success / len(expected_dollars))))
    print('SUBTOTAL', subtotal)
