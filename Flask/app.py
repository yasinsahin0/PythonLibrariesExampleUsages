from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    # ana url tıkladığımızda ekrana hello world yazısını bastırır.
    return "Hello, World!"

@app.route("/<name>")
def hello(name):
    # name gelen parametre olarak alınır ve üzerinde işlem yapılabilir.
    return f"Hello, {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Gelen değer integer olarak alınır.
    print(type(post_id))
    return f'Post {post_id}'

app.add_url_rule("/", endpoint="index")
@app.endpoint("index")
def index():
    return "indexx"

@app.route('/NameSurname',methods=['POST'])
def var_resp():
    name = request.form['name']
    surname = request.form['surname']
    # print("Name : {0}, Surname : {1}".format(name,surname))
    top_str = name + " " + surname
    return top_str

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # Gelen değer bir string'dir.
    print(type(subpath))
    return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Post atıldı"
    else:
        return "Post atılmadı !"

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return "Hata : 404"

@app.errorhandler(500)
def page_not_found(error):
    print(error)
    return "Hata : 500"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)