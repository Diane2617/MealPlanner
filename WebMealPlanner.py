#import Flask class
from fileinput import filename
from tokenize import Name
from flask import Flask, request, render_template


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def WelcomeGreeting():
    return render_template('home.html')

    
#      f'''
#     <h1>Welcome to the Meal Planner!<h1>
#     <p>I can take the headache out of deciding what to cook. You may choose to have
#     a standard meal which is a protein, a method of preparation, two sides and a vegetable. 
#     Alternatively, you may choose how many sides and vegetable you wish to have with your meal.</p>
    
#     <p><a href="standard">Standard Meal</a></p>

#     <p><a href="custom">Custom Meal</a></p>

# '''
@app.route('/custom')
def customMeal():
  return render_template('meal_info.html', choice='custom')

@app.route('/standard')
def standard():
  return render_template('meal_info.html', choice='standard')

@app.route('/yourbuild')
def yourMeal():
  return render_template('meal_info.html')

  
@app.route('/meal', methods=["GET", "POST"])
def mealshow():
  mealdisplay = meal_generator(int(request.form["NumDays"]), int(request.form.get("CustomSides", 2)), int(request.form.get("CustomVege", 1)))
  #return render_template('meal_display.html')
  return f'''<p> Hi {request.form["Name"]} your meals are:
     <ul>
     {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
     </ul> </p> '''
   


if __name__ == '__main__':
    app.run(threaded=True)