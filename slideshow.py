# this is where the magic happens
import networkx as nx
from slide import Slide, Image



def gen_slideshow(slides):
    G = nx.complete_graph(len(slides))
    for e in G.edges():
        print(e)

def main():
    images = []
    images.append(Image(0, True, {'hello', 'world'}))
    images.append(Image(1, True, {'hello', 'world', 'goodbye'}))
    images.append(Image(2, True, {'hello', 'jimmy', 'johns'}))
    images.append(Image(3, True, {'cs374', 'uiuc'}))
    images.append(Image(4, True, {'adrian', 'dylan', 'joe'}))
    images.append(Image(5, True, {'hash', 'code'}))
    images.append(Image(6, True, {'girls', 'who', 'code'}))
    images.append(Image(7, True, {'new', 'phone', 'who', 'dis'}))
    images.append(Image(8, True, {'dis', 'track' }))

    slides = []
    for image in images:
        slides.append(Slide(image))

    gen_slideshow(slides)


main()
    


