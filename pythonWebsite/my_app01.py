# -*- coding: <utf-8> -*-
"""
Created on Sat Oct 17 14:51:52 2015

@author: roxanaohriniuc
"""

from flask import Flask, render_template

app = Flask(__name__)

class Post:
    name = "name"
    text = "text"
    def __init__(self, post_name):
        if (post_name =="Python"):
            self.name = post_name
            self.text = """Python is too cool for school."""
        elif (post_name =="About"):
            self.name = "About"
            self.text = """ 
            Well.. please click the "About" page above. It will have more information on the subject
            """
        elif (post_name == "Projects"):
            self.name = post_name
            self.text = """ 
            I am currently working on building the next Google!....:D:D::D
            """
        else:
            self.name = "Uh-oh"
            self.text = """I haven't written about this.... yet!"""

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/post', methods = ['GET'])
def post_page():
    return render_template('post.html')  

@app.route('/post/<name>', methods = ['GET'])
def postname_page(name):
    return render_template('post.html', post = Post(name))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home_page(path):
    return render_template('home.html') 

app.run(debug = True,port=5500, host='0.0.0.0') 