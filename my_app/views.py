# Views at the end of Workshop 2

from my_app import app, db
from flask import render_template, request, redirect
from my_app.models import Fact, Post

name="Justin Yu"

@app.route("/")
def index():
    db_facts = Fact.query.all()
    db_posts = Post.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}
    post_list = [{'title': post.title, 'description': post.description} for post in db_posts]
    return render_template("index2.html", name=name, facts=fact_dict, posts=post_list)

@app.route("/change_name")
def change_name():
    global name
    new_name = request.args.get('name')
    name = new_name
    return redirect("/")

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        post_info = request.get_json()
        new_post = Post(title=post_info['title'], description=post_info['description'])
        db.session.add(new_post)
        db.session.commit()
    return redirect("/")


# this will be an exercise 
@app.route("/change_facts", methods=["POST"])
def change_facts():
    if request.method == "POST":
        change_facts = request.get_json()
        for key, value in change_facts.items():
            if Fact.query.filter(Fact.name == key).first() is None:
                new_fact = Fact(name=key, value=value)
                db.session.add(new_fact)
            db.session.commit()
            
    return redirect("/")
