#import Flask class
from flask import Flask, request


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def WelcomeGreeting():
    return f'''<h1>Welcome to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. 
I can give you a protein, and a method of preparation, with two sides.
Alternatively, I can build a meal to your preference. <p>

<form action="/meal" method="POST">
    <h3>Input some information to help me get you started</h3>
    <p>
      <label for="Meal">Your Name:</label>
      <input type="text" name="Name"/>
    </p>
    <p>
      <label for="NumDays">Number of days you would like the meal for:</label>
      <input type="number" name="NumDays"/>
    </p>

    <input type="submit"/> 
</form>
'''


@app.route('/meal', methods=["GET", "POST"])
def mealshow():
    mealdisplay = meal_generator(int(request.form["NumDays"]))
    return f'''<p> Hi {request.form["Name"]}
    <ul>
    {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
  
   
</ul> </p>'''

@app.route('/custom')
def customMeal():
  pass

if __name__ == '__main__':
    app.run(threaded=True)