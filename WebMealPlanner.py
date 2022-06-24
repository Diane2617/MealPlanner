#import Flask class
from flask import Flask

#Create Flask object
app = Flask(__name__)

@app.route('/home')
def WelcomeGreeting():
    return f'''<h1>Welcome to the Meal Planner!<h1>
    <p>I can take the headache out of deciding what to cook. 
I will give a a protein, and a method of preparation, with two sides.<p>'''