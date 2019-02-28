import pair_vertical
import sys
import slideshow

sys.stdout=open("a_out.txt","w")
print(get_results("input_output/a_example.txt"))
sys.stdout.close()

sys.stdout=open("b_out.txt","w")
print(get_results("input_output/b_lovely_landscapes.txt"))
sys.stdout.close()

sys.stdout=open("c_out.txt","w")
print(get_results("input_output/c_memorable_moments.txt"))
sys.stdout.close()

sys.stdout=open("d_out.txt","w")
print(get_results("input_output/d_pet_pictures.txt"))
sys.stdout.close()

sys.stdout=open("e_out.txt","w")
print(get_results("input_output/e_shiny_selfies.txt"))
sys.stdout.close()


def get_results(input_file):
    slides = pair_vertical.pair(input_file)
    slides = slideshow.gen_slideshow(slides)
    output = "" + str(len(slides)) + "\n"
    for slide in slides:
        output += str(slide.image1.img_id)
        if (not horizontal):
            output += str(slide.image2.img_id)
        slide += "\n"
    return output
