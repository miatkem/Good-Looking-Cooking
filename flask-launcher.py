import flask
import os
from recipe import Recipe, searchRecipes
from twitter import Tweet, getTweet

'''
template_dir = os.path.abspath('../html')
'''
#function to generate tweets using the 'twitter.py' functions and address the error of if no tweets can be found
def generateTweets(recipe):
    tweets=getTweet(""+recipe.name+" -politics -filter:retweets",3,recipe.foodKeyWords)
    if len(tweets)==0:
        tweets.append(Tweet("","No tweets found",""))
    return tweets

#initialize flask app
app = flask.Flask(__name__)

#index screen - prompts user to login or signup
@app.route('/')
def index():
    return flask.render_template('index.html')

#login screen - prompts user for email and password
@app.route('/login')
def login():
    #WRITE CODE TO CHECK CREDENTIALS HERE
    return flask.render_template('login.html')

#signup screen - prompts user for email, name, and password
@app.route('/signup')
def signup():
    #WRITE CODE TO CHECK CREDENTIALS HERE
    return flask.render_template('signup.html')

#profile screen - NOT YET DEVELOPED - will allow user to see liked recipes and update profile info
@app.route('/profile')
def profile():
    return flask.render_template('profile.html')

#recipe screen - a detailed page with tweets and recipe information about a singualar recipe
@app.route('/recipe')
def recipe():
    recipeName = flask.request.args['recipeName']
    recipe = searchRecipes(recipeName)[0]
    tweets = generateTweets(recipe)
    return flask.render_template('recipe.html',
    recipe=recipe,
    tweets=tweets)

#recipe screen - a page with search results of up to 10 recipes. Each recipe has a small amount of 
#                information displayed, but clicking a recipe with bring you the detailed recipe page
@app.route('/search-results', methods=["GET", "POST"])
def searchResults():
    query=''
    #get query if button is clicked
    if flask.request.method == "POST":
        #get query from search form
        req = flask.request.form
        query = req["search"]
    else: #get query if 'enter' is pressed
        query = flask.request.args['search']
    
    #search recipes using 'recipe.py'
    recipes = searchRecipes(query,False) #extended=False to only parse information necessary
    
    #if at least on recipe was found, load those recipes on the 'search-results.html'
    if(len(recipes)>0):
        return flask.render_template('search-results.html',
        recipes=recipes,
        query=query)
    else:   #if failed to find results, route back home
        return flask.render_template('home.html')

#home screen - a page with a search bar, random button, and some preset categories to assist in user
#              exploration of the web app
@app.route('/home')
def home():
    return flask.render_template('home.html')

#random recipe - this route generate a random recipe using spoonacular and than routes to a recipe page
#                about the random recipe
@app.route('/random-recipe')
def ranRecipe():
    #search a random recipe and generate tweets for it
    recipe = searchRecipes("random")[0]
    tweets = generateTweets(recipe)
    return flask.render_template('recipe.html',
    recipe=recipe,
    tweets=tweets)

#run the app on port 8080
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP','0.0.0.0')
)