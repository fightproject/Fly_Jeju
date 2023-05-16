from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("doc2vec_model.pkl", "rb") as f:
    doc_vectorizer = pickle.load(f)

@app.route('/',methods=['GET','POST'])
def first_index():

    return render_template('first_page.html')


# 아래 주석을 풀고, 웹 애플리케이션을 실행해 보세요.
if __name__ == "__main__":
    app.run(debug=True)