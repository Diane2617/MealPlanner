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

    <p><a href="customMeal">Custom Meal</a></p>

'''
@app.route('/custom')
def customMeal():
  pass

@app.route('/standard')
def standard():
  return f'''
  <form action="/meal" method="POST">
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

@app.route('/meal', methods=["GET", "POST"])
def mealshow():
#  standardMeal = request.form["Standard"]

#  {% if standardMeal == "Yes"}
  mealdisplay = meal_generator(int(request.form["NumDays"]), 2, 1)
  return f'''<p> Hi {request.form["Name"]} your meals are:
    <ul>
    {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
    </ul> </p> '''
#  {% else %}
#    mealdisplay = meal_generator(int(request.form["NumDays"]), int(request.form[2, 1)
#      return f'''<p> Hi {request.form["Name"]}
#      <ul>
#      {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
#      </ul> </p> '''

#  {% endif %}  
   


if __name__ == '__main__':
    app.run(threaded=True)