#import Flask class
from tokenize import Name
from flask import Flask, request


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)

@app.route('/')
def InitialGreeting():
    return  f'''<form action="/home" method="POST">
    <h3>Hi, what's your name?</h3>
    <p>
      <label for="Meal">Your Name:</label>
      <input type="text" name="Name"/>
    </p>
    <input type="submit"/> 
    </form>
    '''


@app.route('/home')
def WelcomeGreeting():
    return f'''<h1>Welcome {request.form["Name"]} to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. You may choose to have
    a standard meal which is a protein, a method of preparation, two sidese and a vegetable. 
    Alternatively, you may choose how many sides and vegetable you wish to have with your meal.<p>

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