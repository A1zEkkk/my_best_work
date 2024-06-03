import text
import nltk
import pymorphy2

nltk.download("stopwords")
nltk.download("punkt")

from nltk.corpus import stopwords
from string import punctuation, digits

stopwords_ = stopwords.words("russian")
morph = pymorphy2.MorphAnalyzer()

words1 = text.text1.split()
morphing = []

words_aft_iter = ''

for i in words1:
    zero_phorm = morph.parse(i)[0].normal_form
    if zero_phorm not in stopwords_:
        for j in zero_phorm:
            if j not in punctuation and j not in digits:
                words_aft_iter += j
        morphing.append(words_aft_iter)
        words_aft_iter = ''

string_morph = " ".join(morphing)



