import requests
import os
import spoonacular as sp

#Recipe object - holds recipe data so that recipes can be moved around in a more
#               light weight data structure in flask
class Recipe:
    #class variables
    name=""
    decription=""
    timeToCook=""
    ingredients=""
    servings=""
    steps=""
    image=""
    link=""
    foodKeyWords=[]
    
    #oject is initialized by a json object that contains recipe information
    def __init__(self, recipeJson, extended=True): #extended is used for when all info about a recipe is needed
        #Initialize variables with simple reading of json
        self.name = recipeJson["title"]
        self.description = recipeJson["summary"]
        self.timeToCook = str(recipeJson["readyInMinutes"]) + " mins"
        try:
            self.image = recipeJson["image"]
        except: #if
            self.image = "../static/star.svg"
            
        #function to parse ingrdients and amounts from recipe json
        def parseIngrdients(recipeJson):
            ingredients = recipeJson["extendedIngredients"]
            result = []
            for ing in ingredients:
                strIngredient = str(ing["measures"]["us"]["amount"]) + " " + ing["measures"]["us"]["unitShort"] +" of " +ing["name"]
                result.append(strIngredient)
            return result
        self.ingredients = parseIngrdients(recipeJson)
        self.amtIngredients = len(self.ingredients)
        
        
        
        #include information needed for full recipe page
        if extended:
            
            #Initialize variables with simple reading of json
            self.link = recipeJson["sourceUrl"]
            self.servings = str(recipeJson["servings"])
            
            #parse instruction from recipe json
            self.steps = []
            if(len(recipeJson["analyzedInstructions"])>0):
                instructions = recipeJson["analyzedInstructions"][0]["steps"]
                for step in instructions:
                    self.steps.append(step["step"])
                    
            #use spoonacular to detect the food keywords in the recipe description
            def getFoodWords(text):
                api_key = os.environ['SPOON_API_KEY']
                api = sp.API(api_key)
                response = api.detect_food_in_text(self.description)
                data = response.json()
                foodwords= []
                for a in data['annotations']:
                    foodwords.append(a['annotation'])
                return foodwords
            self.foodKeyWords = getFoodWords(self.description)

#function to search for recipes in spoonacular given a query string
def searchRecipes(query, extended=True):
    
    #initilize api_key and spoonacular object
    api_key = os.environ['SPOON_API_KEY']
    api = sp.API(api_key)
    
    #request recipes from spoonacular using query
    if query=="random": #get one random recipe
        response = api.get_random_recipes(True,1)
        data = response.json()
        recipes = data["recipes"]
    else: #get recipes based on query
        response = api.search_recipes_complex(query)
        data = response.json()
        recipes = data["results"]
    
    #extract recipe id(s) from json response
    ids=""
    for rec in recipes:
        ids+=""+str(rec["id"])+","
    
    #use id(s) to capture a more detailed json response about a recipe
    response = api.get_recipe_information_bulk(ids)
    data = response.json()
    
    #create a list of recipe objects that are intialized by the json objects in data
    recipes = []
    
    #check if search failed
    try:
        if data['status'] == 'failure':
            return recipes
    #if there is no status then it was succesful, create recipes
    except:
        for recipeJson in data:
            recipes.append(Recipe(recipeJson,extended))
        return recipes