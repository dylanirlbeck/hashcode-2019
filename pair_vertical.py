import random
from input_output.input_script import get_vh
from slide import Image
from slide import Slide

def pair_vertical(input_file):
    slides = []
    vertical, horizontal = get_vh("input_output/" + input_file)
    while (len(vertical) > 0):
        rand_int = random.randint(1, len(vertical))
        Image1 = Image(vertical[0][0], False, vertical[0][1])
        Image2 = Image(vertical[rand_int][0], False, vertical[rand_int][1])
        Slide = Slide(Image1, Image2)
        slides.append(Slide)
        vertical.pop(0)
        vertical.pop(rand_int - 1)

    for i in range(len(horizontal)):
        Image_horizontal = Image(horizontal[i][0], True, horizontal[i][1])
        Slide_h = Slide(Image_horizontal)
    slides.append(Slide_h)

def merge(tags_1, tags_2): ## merging the tags of two vertical photos
    tag_set = {}
    for i in range(len(tags_1)):
        tag_set.add(tags_1[i])

    for i in range(len(tags_2)):
        tag_set.add(tags_2[i])

    return list(tag_set)
