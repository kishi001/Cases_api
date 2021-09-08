from flask import Flask, request, render_template, jsonify
from flask import Blueprint, jsonify
app = Flask(__name__)
app.secret_key = 'secret'
from collections import OrderedDict
from process import Case
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string


@app.route('/TitleCase', methods=['GET', 'POST'])
def titleCase():
    if request.method == 'POST':
        data = request.get_json()
        text = data["text"]

        c1 = Case()
        #out_lst = list()
        SC_list = c1.titleCase(text)


        # print("".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in fc_lst]).strip())
        print(TreebankWordDetokenizer().detokenize(SC_list))

        return jsonify({"output": (TreebankWordDetokenizer().detokenize(SC_list))})
    else:
        return jsonify({"status":"fail", "error_log":"check post request"})


# serve at localhost:5444
if __name__ == "__main__":
    app.run(port=5444)
