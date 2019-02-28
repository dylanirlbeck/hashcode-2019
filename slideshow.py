# this is where the magic happens
import networkx as nx
from slide import Slide, Image


def gen_slideshow(slides):
    n = len(slides)
    G = nx.complete_graph(n)
    nodes = list(G.nodes())
    start_weights = {}
    for x in range(n):
        for y in range(n):
            start_weights[(x, y)] = 0

    nx.set_edge_attributes(G, start_weights, "interest")
    zero_edges = []
    for e in G.edges():
        (x, y) = (e[0], e[1])
        interest = slides[x].get_interest(slides[y])
        if interest == 0:
            zero_edges.append((x,y))
    
    G.remove_edges_from(zero_edges)
    for e in G.edges():
        (x, y) = (e[0], e[1])
        interest = slides[x].get_interest(slides[y])
        print(str(slides[x].get_tags()) + ", " + str(slides[y].get_tags()) + str(interest))

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
    images.append(Image(8, True, {'dis', 'track'}))

    slides = []
    for image in images:
        slides.append(Slide(image))

    gen_slideshow(slides)


    


