#!/usr/bin/python3
''' Script to validate a data set's UTF-8 encoding. '''


def validUTF8(data):
    '''Determines if a given data set represents
    a valid UTF-8 encoding.
    '''
    byte_size = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for d in data:
        mask_byte = 1 << 7

        if byte_size == 0:
            while mask_byte & d:
                byte_size += 1
                mask_byte = mask_byte >> 1

            if byte_size == 0:
                continue

            if byte_size == 1 or byte_size > 4:
                return False

        else:
            if not (d & mask_1 and not (d & mask_2)):
                return False

        byte_size -= 1

    if byte_size == 0:
        return True

    return False
