import random
from slide import Image

images = []
while (len(vertical) > 0):
    rand_int = random.randint(1, len(list))
    ids = (id_1 = list[0][0], list[rand_int][0])
    tags = merge(list[0][1], list[rand_int][1])
    images.append(Image(ids, False, tags))
    list.pop(0)
    list.pop(rand_int - 1)

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
