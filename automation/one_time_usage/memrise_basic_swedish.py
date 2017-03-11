from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

f = open("memrise_basic_swedish.csv", "w")

for page in range(1, 42):
    # f.write("-_-_-_-_-_ nivå {0} -_-_-_-_-_, -_-_-_-_-_ Level {1} -_-_-_-_-_\n".format(page, page))
    html = urlopen("http://www.memrise.com/course/806/basic-swedish/" + str(page) + "/")
    html_obj = BeautifulSoup(html.read(), "html.parser")
    swedish_word_list = html_obj.findAll("div", {"class": "col_a col text"})
    english_word_list = html_obj.findAll("div", {"class": "col_b col text"})

    for i in range(len(swedish_word_list)):
        swedish_word = re.sub(",", ";", swedish_word_list[i].get_text())
        english_word = re.sub(",", ";", english_word_list[i].get_text())

        f.write("{0}, {1}\n".format(swedish_word, english_word))

f.close()
