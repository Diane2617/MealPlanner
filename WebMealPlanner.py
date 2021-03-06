#import Flask class
from tokenize import Name
from flask import Flask, request


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def WelcomeGreeting():
    return f'''<h1>Welcome to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. You may choose to have
    a standard meal which is a protein, a method of preparation, two sides and a vegetable. 
    Alternatively, you may choose how many sides and vegetable you wish to have with your meal.</p>
    
    <p><a href="standard">Standard Meal</a></p>

    <p><a href="custom">Custom Meal</a></p>

'''
@app.route('/custom')
def customMeal():
  return f'''
  <form action="/mealcustom" method="POST">
    <h3>Input some information to help me create your custom meal.</h3>
    <p>
      <label for="Name">Your name:</label>
      <input type="text" name="Name"/>
    </p>
    <p>
      <label for="NumDays">Number of days you would like the meal for:</label>
      <input type="number" name="NumDays"/>
    </p>

    <p>
      <label for="CustomSides">Number of sides:</label>
      <input type="number" name="CustomSides"/>
    </p>

    <p>
      <label for="CustomVege">Number of veges:</label>
      <input type="number" name="CustomVege"/>
    </p>
    <input type="submit"/> 
</form>
  '''

@app.route('/standard')
def standard():
  return f'''
  <form action="/mealstandard" method="POST">
    <h3>Input some information to help me get you started</h3>
    <p>
      <label for="Name">Your name:</label>
      <input type="text" name="Name"/>
    </p>
    <p>
      <label for="NumDays">Number of days you would like the meal for:</label>
      <input type="number" name="NumDays"/>
    </p>

    <input type="submit"/> 
  </form>
  '''

@app.route('/mealstandard', methods=["GET", "POST"])
def mealshow():
  mealdisplay = meal_generator(int(request.form["NumDays"]), 2, 1)
  return f'''<p> Hi {request.form["Name"]} your meals are:
    <ul>
    {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
    </ul> </p> '''

@app.route('/mealcustom', methods=["GET", "POST"])
def customshow():
  mealdisplay = meal_generator(int(request.form["NumDays"]), int(request.form["CustomSides"]), int(request.form["CustomVege"]))
  return f'''<p> Hi {request.form["Name"]} your meals are:
    <ul>
    {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
    </ul> </p> '''

   


if __name__ == '__main__':
    app.run(threaded=True)