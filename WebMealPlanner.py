#import Flask class
from flask import Flask, request


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def WelcomeGreeting():
    return f'''<h1>Welcome to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. 
I will give a a protein, and a method of preparation, with two sides.<p>

<form action="/" method="POST">
    <h3>Input some information to help me get you started</h3>
    <p>
      <label for="Meal">Your Name:</label>
      <input type="text" name="Name"/>
    </p>
    <p>
      <label for="NumDays">Number of days you would like the meal for:</label>
      <textarea name="NumDays"></textarea>
    </p>
</form>

<a href="/meal">Generate meal</a>
'''


@app.route('/meal')
def mealshow(NumDays):
    mealdisplay = meal_generator(NumDays)
    return f'<p> {mealdisplay} </p>'
