import os
from collections import Counter
book_dir="C:/Users/leons/Desktop/Codefiles-Testing-and-Debugging/Translation/Books"
import pandas as pd
def read(file):
    with open(file, "r", encoding="utf8") as f:
        s=f.read()
    s=s.replace("\n","")
    s=s.replace("\r","")
    return s


def count_words(s):
    s=s.lower()
    skips=[",",".","!",";","'",'"',":"]
    for c in skips:
        s=s.replace(c, "")
    wrds_dic= Counter(s.split(" "))
    return wrds_dic


def wrds_stats(w_c):
    num_unique=len(w_c)
    counts=w_c.values()
    return(num_unique, counts)
    
    
stats=pd.DataFrame(columns=("Language", "author", "titlr", "length", "unique"))
title_num=1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language+ "/" + author):
            input_file=book_dir + "/" + language+ "/" + author + "/" + title
            s=read(input_file)
            (num_unique, counts)= wrds_stats(count_words(s))
            stats.loc[title_num]= language, author.capitalize(), title.replace(".txt"," "), sum(counts), num_unique
            title_num+=1
print(stats.head())
print(stats.tail())