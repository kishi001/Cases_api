from collections import OrderedDict
from process import Case
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string
import pandas as pd

data = pd.read_excel("TiteCase.xlsx")

out_lst = []
for i in data["Text"]:
#text = "The RS NDVI data include the Global Inventory at India"
    text=str(i)
    c1 = Case()
    SC_list = list()
    type = "title"

    if type=="title":
        SC_list = c1.titleCase(text)
    else:
        SC_list = c1.sentenceCase(text)


    #print("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in fc_lst]).strip())
    print(TreebankWordDetokenizer().detokenize(SC_list))
    out_lst.append(TreebankWordDetokenizer().detokenize(SC_list))

data["output"] = out_lst
data.to_excel("out.xlsx", index=False)