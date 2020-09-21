import requests
import os
import spoonacular as sp


class Recipe:
    
          
    #ingredients
    name=""
    decription=""
    timeToCook=""
    ingredients=""
    servings=""
    steps=""
    image=""
    link=""
    
    def __init__(self, recipeJson):
        #name 
        self.name = recipeJson["title"]
        
        #description
        self.description = recipeJson["summary"]
        
        #timetocook
        self.timeToCook = str(recipeJson["readyInMinutes"]) + " mins"
        
        #ingredients
        def parseIngrdients(recipeJson):
            ingredients = recipeJson["extendedIngredients"]
            result = []
            for ing in ingredients:
                strIngredient = str(ing["measures"]["us"]["amount"]) + " " + ing["measures"]["us"]["unitShort"] +" of " +ing["name"]
                result.append(strIngredient)
            return result
            
        self.ingredients = parseIngrdients(recipeJson)
        self.amtIngredients = len(self.ingredients)
        
        #sevings
        self.servings = str(recipeJson["servings"])
        
        #instructions
        self.steps = []
        if(len(recipeJson["analyzedInstructions"])>0):
            instructions = recipeJson["analyzedInstructions"][0]["steps"]
            for step in instructions:
                self.steps.append(step["step"])
        
        #image
        try:
            self.image = recipeJson["image"]
        except:
            self.image = "../static/star.svg"
        
        #link 
        self.link = recipeJson["sourceUrl"]
    
  

def searchRecipes(query):
    api_key = os.environ['SPOON_API_KEY']
    api = sp.API(api_key)
    ids=""
    if query=="random":
        response = api.get_random_recipes(True,1)
        data = response.json()
        recipes = data["recipes"]
    else:
        response = api.search_recipes_complex(query)
        data = response.json()
        recipes = data["results"]
    
    ids=""
    for rec in recipes:
        ids+=""+str(rec["id"])+","
            
    response = api.get_recipe_information_bulk(ids)
    
    data = response.json()
    
    recipes = []
    for recipeJson in data:
        recipes.append(Recipe(recipeJson))
    return recipes
    
# TEST CODE
#rs=searchRecipes("apple")
#for r in rs:
#    print(r.name,r.decription,r.timeToCook,r.ingredients,r.servings,r.steps,r.image,r.link)
