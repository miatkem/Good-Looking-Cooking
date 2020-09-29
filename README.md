# Welcome to the Good Looking Cooking app repository. 

This is a web app that allows users to navigate the spoonacular recipe database and find useful recipes.

Note: The CSS is optimized so that it looks best on a mobile device currently. To use it how its meant
to be used, press F12 in chrome, press the phone/tablet icon to the left of the 'elements' tab on the right
side of the screen, and select IPhone X from the drop down in the top center of the screen. It is still
navigatable in a normal desktop view, just not as pleasing to the eye.

Note: There should be no problems with this project

## <b>To set up the app on your server follow these steps:</b>

### Step 1 - Setup Twitter API <br/>
1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    If needed, you can regenerate your access token and secret.
4. Create a file in the root directory called twitter.env with key and tokens. It should be formmatted like:<br/>
    export TWITTER_ACCESS_TOKEN='[your access token here]'<br/>
    export TWITTER_ACCESS_TOKEN_SECRET='[your secret access token here]'<br/>
    export TWITTER_API_KEY='[your key here]'<br/>
    export TWITTER_API_KEY_SECRET='[your secret ket here]'<br/>

### Step 2 - Setup Spoonacular API
1. Sign up for the api at https://spoonacular.com/food-api/console#Dashboard
2. Navigate to https://spoonacular.com/food-api/console#Profile to find your api key
3. Create a file in the root directory called spoon.env with the key. It should be formmatted like:<br/>
    export SPOON_API_KEY='[your api key here]'

### Step 3 - Clone Repository
1. Open a terminal in your environment
2. Clone this repository using git clone https://github.com/NJIT-CS490/project1-mdm56

### Step 4 - Install python dependencies
1. Install Flask using 'sudo pip install flask'
2. Install requests using 'sudo pip install requests'
3. Install spoonacular wrapper using 'sudo pip install spoonacular'

### Step 5 - Sourcing API Keys
1. In the terminal source the twitter keys by using 'source twitter.env'
2. In the terminal source the spoonacular key by using 'source spoon.env'

### Step 6 - Start the flask app in your environment
1. Navigate to the root directory of the project
2. Run flask-launcher.py using the terminal command 'python flask-launcher.py'
3. The app is now running locally and you should be able to see it using your local ip and port 8080
    If you are running on aws, simply click preview to see the web app
   
### Step 7 - Run the app on Heroku
1. Sign up for heroku at heroku.com 
2. Install heroku in your terminal by running npm install -g heroku
3. Name the app 'goodlookingcooking'
4. Go through the following steps:
    heroku login -i
    heroku create
    git push heroku master
5. Add secret keys (from twitter.env and spoon.env) by going to https://dashboard.heroku.com/apps
    and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
    "Reveal Config Vars" and add the key value pairs for the five keys (use the same key names)
6. In terminal push again to start app again with the command 'git push heroku master'
   

IMPORTANT NOTE: Be sure that you name the env files correctly since those specific file names are
included in the .gitignore file to prevent any keys from being pushed to a public repo.

## <b>Functionality of Good Looking Cooking</b>

<b>Feature 1 - Login Page</b><br/>
    Right now the login page is not setup to actually check any credentials. oAuth maybe implemented in a later date.
    Simply navigate through by pressing login or sign up and then submitting the empty form.

<b>Feature 2 - The Home Screen</b><br/>
    The home screen has some preset categories. Click one to find the search results for 'lunch', 'dinner, ect.
    To return to home at anytime, simply click the logo in the top left corner

<b>Feature 3 - Search Bar</b><br/>
    The search bar allows the user to search the spoonacular api for specific recipies.
    Simply press enter or click the magnifing glass to make the search and at most 10 results will show up 
    Once in the search screen you can select a recipe by clicking on it to go to the recipe page
    
<b>Feature 4 - The Randomizer</b><br/>
    In the center of the screen is what looks to be a refresh buttun. Clicking that will bring 
    you to a recipe page of a random recipe

<b>Feature 5 - Tweets</b><br/>
    On recipe pages Twitter API is used to find relevant tweets, first by searching the name of the
    recipe and if none exist it then searches by using key words from the recipe description.

<b>Feature 6 - Responsive CSS</b><br/>
    The css is repsonsive using media queries to make the web app more responsive to larger screen. It was 
    built mobile first and looks best on mobile but this css makes desktop viable.

## <b>Future features to add</b>

<b>Feature 1 - Assisted Search</b><br/>
    Using Spoonacular the seach bar can be improved to suggest search queries as the user types their own

<b>Feature 2 - Suggested Recipes</b><br/>
    Using Spoonacular recipies can be suggested on a recipe page based on the current recipe and the results
    can appear at the bottom of the page to improve user exploration of the recipe catalog

<b>Feature 3 - User Accounts</b><br/>
    Using a database, user accounts can be saved and used to access the app that way users can like recipes
    so that they can be used again later. The popular catergory on the home screen could then be used to
    display recipes with the most likes on the app.

## <b>Challenges</b>

<b>Challenge 1 - Using Twitter API</b><br/>
    I decided to use requests to call the twitter API. This was challenging and took a bit of research to learn
    how to do. Harder than just making the call was parsing the data from JSON response. I solved this issue by
    going into the API doc and reading how the JSON data is structured. This took a bit of time for me to get right.
    
<b>Challenge 2 - Parsing Ingredients</b><br/>
    Ingredients were a little tricky to parse from the Spoonacular API. Again, I had to go scouring through the 
    API docs to find how its structured. I wanted to have amount included so I had to turn the name and amount 
    into a contatenated string.
    
<b>Challenge 3 - Spoonacular Search Limits</b><br/>
    I wanted to go a above the specifications for this project and give the user the ability to search for
    recipes. Doing this increased the rate I would use up my daily spoonacular requests, so I began to run out
    pretty quickly. To solve this I decided to upgrade my API access and pay the very minimal amount of money
    to have more requests. I felt this was worth it since I will be adding this project to my personal 
    portfolio.

   
