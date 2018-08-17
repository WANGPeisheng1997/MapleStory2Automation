from PIL import Image, ImageGrab
import math
import operator
from functools import reduce
from dHash import DHash
# def get_image_histogram(imgobj):
#     return imgobj.histogram()
#
#
# def pil_image_similarity(h1, h2):
#     rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
#     return rms
#
#
# def avhash(im):  # 通过计算哈希值来得到该张图片的“指纹”
#     if not isinstance(im, Image.Image):  # 判断参数im，是不是Image类的一个参数
#         im = Image.open(im)
#     im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
#     avg = reduce(lambda x, y: x + y, im.getdata()) / 64.  # 递归取值，这里是计算所有
#     return reduce(lambda x, (y, z): x | (z << y), enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())), 0)
#
#
# def hamming(h1, h2):
#     h, d = 0, h1 ^ h2
#     while d:
#         h += 1
#         d &= d - 1
#     return h


# coordinate = (0, 0, 1000, 1000)
# pic = ImageGrab.grab(coordinate)
# pic.save("123.jpg")
# pic.save("123.png")
# pic2 = Image.open("123.jpg")

# h_pic = get_image_histogram(pic)
# print(len(h_pic), h_pic)
# h_ori = get_image_histogram(Image.open("123.jpg"))
# print(len(h_ori), h_ori)
#
# print(pil_image_similarity(h_pic, h_ori))
pic = Image.open("timg.jpg")
pic2 = Image.open("timg2.jpg")

dHash1 = DHash.calculate_hash(pic, "p")
dHash2 = DHash.calculate_hash(pic2, "j")
hamming_distance = DHash.hamming_distance(dHash1, dHash2)
print(hamming_distance)
