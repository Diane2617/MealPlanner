#import Flask class
from fileinput import filename
from tokenize import Name
from flask import Flask, request, render_template


# import function from mealplanner
from MealPlanner import Meal, meal_generator

#Create Flask object
app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def WelcomeGreeting():
    return render_template('home.html')

    
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
  #return render_template('meal_display.html',mealdisplay=mealdisplay)
  return f'''<p style = "font-family:georgia,garamond,serif;font-size:25px;font-style:italic; text-align: justify"> Hi {request.form["Name"]} your meals are:</p>
      <ul>
      
       {"".join([f"<li>{meal}</li>" for meal in mealdisplay])}
     </ul> </p> '''
   


if __name__ == '__main__':
    app.run(threaded=True)