#import Flask class
from flask import Flask, request


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def WelcomeGreeting(env,respond):
    return f'''<h1>Welcome to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. 
I will give a a protein, and a method of preparation, with two sides.<p>

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
    return f'''<p> 
    <ul>
    {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
  
   
</ul> </p>'''

if __name__ == '__main__':
    app.run(threaded=True)