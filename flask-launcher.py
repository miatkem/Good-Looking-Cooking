import flask
import os
from recipe import Recipe, searchRecipes
from twitter import Tweet, getTweet

'''
template_dir = os.path.abspath('../html')
'''
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')
    
@app.route('/login')
def login():
    return flask.render_template('login.html')
    
@app.route('/signup')
def signup():
    return flask.render_template('signup.html')
    
@app.route('/profile')
def profile():
    return flask.render_template('profile.html')
    
@app.route('/recipe')
def recipe():
    recipeName = flask.request.args['recipeName']
    tweets=getTweet(""+recipeName+" -politics -filter:retweets",3)
    if len(tweets)==0:
        tweets.append(Tweet("","No tweets found",""))
        
    recipe = searchRecipes(recipeName)[0]
    return flask.render_template('recipe.html',
    recipe=recipe,
    tweets=tweets)
    
@app.route('/search-results', methods=["GET", "POST"])
def searchResults():
    if flask.request.method == "POST":
        req = flask.request.form
        query = req["search"]
        
        recipes = searchRecipes(query)
        if(len(recipes)>0):
            return flask.render_template('search-results.html',
            recipes=recipes,
            query=query)
    else:
        query = flask.request.args['search']
        recipes = searchRecipes(query)
        if(len(recipes)>0):
            return flask.render_template('search-results.html',
            recipes=recipes,
            query=query)

    return flask.render_template('home.html')
    
@app.route('/home')
def home():
    return flask.render_template('home.html')
    
@app.route('/random-recipe')
def ranRecipe():
    recipe = searchRecipes("random")[0]
    tweets=getTweet(""+recipe.name+" -politics -filter:retweets",3)
    if len(tweets)==0:
        tweets.append(Tweet("","No tweets found",""))
    return flask.render_template('recipe.html',
    recipe=recipe,
    tweets=tweets)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')
)