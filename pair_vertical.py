import random
from input_output.input_script import get_vh
from slide import Image

images = []

file_names = ["a_example.txt", "b_lovely_landscapes", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies"]

for file_name in file_names:
    vertical, horizontal = get_vh("input_output/" + file_name)
    while (len(vertical) > 0):
        rand_int = random.randint(1, len(vertical))
        ids = (vertical[0][0], vertical[rand_int][0])
        tags = merge(vertical[0][1], vertical[rand_int][1])
        images.append(Image(ids, False, tags))
        vertical.pop(0)
        vertical.pop(rand_int - 1)

    for i in range(len(horizontal)):
        id = horizontal[i][0]
        tags = horizontal[i][1]
        images.append(id, True, tags)

    def merge(tags_1, tags_2): ## merging the tags of two vertical photos
        tag_set = {}
        for i in range(len(tags_1)):
            tag_set.add(tags_1[i])

        for i in range(len(tags_2)):
            tag_set.add(tags_2[i])

        return list(tag_set)
