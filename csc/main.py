import nltk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from os import path

import wordcloud
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from zero_word import string_morph


cloud1 = WordCloud(width=1920, height=1080).generate(string_morph)
plt.imshow(cloud1, interpolation="bilinear")
plt.axis("off")
plt.show()


mask = np.array(Image.open(r"C:\Users\Mi\Downloads\guitar.png"))
cloud2 = WordCloud(width=1920, height=1080, mask=mask).generate(string_morph)
plt.imshow(cloud2)
plt.axis('off')
plt.show()