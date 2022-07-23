import random
from num2words import num2words

#List of the types of meat used regularly and different preparation methods

protein = ["Drumsticks", "Thigh", "Wings", "Fish", "Pig tails", "Back & Neck", "Turkey"]
preparation_method = ["Baked", "Fried", "Stewed", "Curried", "Combined with legumes"]

#List of different side dishes 
sides = ["Rice and legumes", "Rice and pink beans", "Vegetable Rice", "Sauteed Macaroni", "Sauteed Sphagetti", "Macaroni Salad",
 "Provision pie", "Macaroni and Cheese pie", "Stuffed Potatoes", "Potato Salad"]

#List of common vegetables
vegetables = ["Lettuce", "Carrot", "Cabbage", "Cucumber", "Pumpkin", "Tomatoes"]



#Function for creating a one day meal plan
class Meal:
    def __init__(self, NumSides, NumVeges):
        meal_meat = random.choice(protein)
        meal_sides = random.sample((sides), k= NumSides)
        meat_prep = random.choice(preparation_method)
        meal_veges = random.sample(vegetables, k= NumVeges)

        
        self.meat = meal_meat
        self.prep = meat_prep
        self.sides = meal_sides
        self.veges = meal_veges
        

    # return true if any of the following properties are the same (meat, prep & sides)
    def hasSameMealProps(self, other_meal):
        if other_meal == None:
            return False
        if other_meal.meat == self.meat:
            return True
        if other_meal.prep == self.prep:
            return True
        if any(s in self.sides for s in other_meal.sides):
            return True
        if any(v in self.veges for v in other_meal.veges):
            return True
        return False

    def Mealdisplay(self, day_count):
        if day_count > 1:
            return f"""For your meal on day {num2words(day_count)}, you will be having {self.prep} {self.meat} with {', '.join(self.sides)} and {', '.join(self.veges)}."""
        else:
            return f"""For this meal you will be having {self.prep} {self.meat} with {', '.join(self.sides)} and {', '.join(self.veges)}."""
            

def meal_generator(num_meals, NumSides, NumVeges, meal_day=1):
    prev_meal = None
    meals = []
    while meal_day <= num_meals:
        
        current_meal = Meal(NumSides,NumVeges)

        # Comparing the items in currnet meal to the previous meal generated
        while current_meal.hasSameMealProps(prev_meal):
            current_meal = Meal(NumSides,NumVeges)
            
        #print out results of meal gernerated
        meals.append(current_meal.Mealdisplay(meal_day))
        # Updating previous meal for next iteration
        prev_meal = current_meal
        meal_day += 1

    return meals

    if num_meals <1:
        print("Do enjoy your meals.")
    else: 
        print("Do enjoy your meal.")

# Run meal function based on user's choice of meal days needed
def meal_print():
    #Welcome message
    welcome_msg = """
I can take the headache out of deciding what to cook. 
I will give a a protein, and a method of preparation, with two sides. 
    
    """
    print(welcome_msg)
    #User to input the number of days for which they would like a 
    # meal plan for
    num_meals = int(input("How many days would you like a meal plan for? "))
    meal_generator(1, num_meals)

print(meal_generator(5, 1, 2))






