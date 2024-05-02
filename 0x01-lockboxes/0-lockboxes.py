#!/usr/bin/python3
"""Script will solve lockboxes (a list of lists)"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for box_key in boxes[key]:
            if box_key not in keys and box_key < len(boxes):
                keys.append(box_key)
    if len(keys) == len(boxes):
        return True
    return False
