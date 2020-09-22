Welcome to the Good Looking Cooking app repository. 

This is a web app that allows users to navigate the spoonacular recipe database and find useful recipes.

Note: The CSS is optimized so that it looks best on a mobile device currently. To use it how its meant
to be used, press F12 in chrome, press the phone/tablet icon to the left of the 'elements' tab on the right
side of the screen, and select IPhone X from the drop down in the top center of the screen. It is still
navigatable in a normal desktop view, just not as pleasing to the eye.

<b>To set up the app on your server follow these steps:</b>

Step 1 - Setup Twitter API 
0. Sign up for the twitter developer portal at https://developer.twitter.com
1. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
2. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
    If needed, you can regenerate your access token and secret.
3. Create a file in the root directory called twitter.env with key and tokens. It should be formmatted like:
    export TWITTER_ACCESS_TOKEN='[your access token here]'
    export TWITTER_ACCESS_TOKEN_SECRET='[your secret access token here]'
    export TWITTER_API_KEY='[your key here]'
    export TWITTER_API_KEY_SECRET='[your secret ket here]'

Step 2 - Setup Spoonacular API
0. Sign up for the api at https://spoonacular.com/food-api/console#Dashboard
1. Navigate to https://spoonacular.com/food-api/console#Profile to find your api key
2. Create a file in the root directory called spoon.env with the key. It should be formmatted like:
    export SPOON_API_KEY='[your api key here]'

Step 3 - Clone Repository
0. Open a terminal in your environment
1. Clone this repository using git clone https://github.com/NJIT-CS490/project1-mdm56

Step 4 - Install python dependencies
0. Install Flask using 'sudo pip install flask'
1. Install requests using 'sudo pip install requests'
2. Install spoonacular wrapper using 'sudo pip install spoonacular'

Step 5 - Sourcing API Keys
0. In the terminal source the twitter keys by using 'source twitter.env'
1. In the terminal source the spoonacular key by using 'source spoon.env'

Step 6 - Start the flask app in your environment
0. Navigate to the root directory of the project
1. Run flask-launcher.py using the terminal command 'python flask-launcher.py'
2. The app is now running locally and you should be able to see it using your local ip and port 8080
    If you are running on aws, simply click preview to see the web app

IMPORTANT NOTE: Be sure that you name the env files correctly since those specific file names are
included in the .gitignore file to prevent any keys from being pushed to a public repo.

<b>Functionality of Good Looking Cooking</b>

Feature 1 - Login Page
    Right now the login page is not setup to actually check any credentials. oAuth maybe implemented in a later date.
    Simply navigate through by pressing login or sign up and then submitting the empty form.

Feature 2 - The Home Screen
    The home screen has some preset categories. Click one to find the search results for 'lunch', 'dinner, ect.
    To return to home at anytime, simply click the logo in the top left corner

Feature 3 - Search Bar
    The search bar allows the user to search the spoonacular api for specific recipies.
    Simply press enter or click the magnifing glass to make the search and at most 10 results will show up 
    Once in the search screen you can select a recipe by clicking on it to go to the recipe page
    
Feature 4 - The Randomizer
    In the center of the screen is what looks to be a refresh buttun. Clicking that will bring 
    you to a recipe page of a random recipe

Feature 5 - Tweets
    On recipe pages Twitter API is used to find relevant tweets, first by searching the name of the
    recipe and if none exist it then searches by using key words from the recipe description.

<b>Future features to add</b>

Feature 1 - Assisted Search
    Using Spoonacular the seach bar can be improved to suggest search queries as the user types their own

Feature 2 - Suggested Recipes
    Using Spoonacular recipies can be suggested on a recipe page based on the current recipe and the results
    can appear at the bottom of the page to improve user exploration of the recipe catalog

Feature 3 - User Accounts
    Using a database, user accounts can be saved and used to access the app that way users can like recipes
    so that they can be used again later. The popular catergory on the home screen could then be used to
    display recipes with the most likes on the app.
    
Feature 4 - Responsive CSS
    Updating css using media queries to make the web app more responsive to larger screen, as it is currently
    optimized for a mobile device.
