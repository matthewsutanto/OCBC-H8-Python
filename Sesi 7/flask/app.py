from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from author_books import author_book
import webbrowser

app = Flask(__name__,template_folder='templates')

@app.route('/home')
@app.route('/')
def home():
    sum=10
    return render_template('index.html')

@app.route('/<string:name>')
def hello(name):
    # return "<h1>Hello "+name+"</h1>"
    return f"Hello, {escape(name)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/hello')
@app.route('/hello/<name>/<id>')
def helloName(name=None,id=None):
    return render_template('index.html',name=name, id=id)


@app.route('/author', methods=['GET','POST'])
def author():
    if 'author_id' in request.form :
        author_book[request.form['author_id']] = [] #empty list
        
    return render_template('author.html', author_book=author_book)

@app.route('/books/<string:author_id>')
def books(author_id):
    html= f'List of books authored by {author_id}:'
    html +="<ul> <li>Buku 1</li> <li>Buku 2</li> </ul>"
    if len(author_book[author_id]) == 0 :
        return render_template('book.html',author_id=author_id)
    else :
        return render_template('book.html', author_id=author_id, book_list=author_book[author_id])
if __name__ == "__main__":
    app.run(debug=True) 
    webbrowser.open_new('http://127.0.0.1:5000/')
