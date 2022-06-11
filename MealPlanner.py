import random

#List of the types of meat used regularly and different preparation methods

meat_kind = ["Drumsticks", "Thigh", "Wings", "Fish", "Pig tails", "Back & Neck", "Turkey"]
preparation_method = ["Baked", "Fried", "Stewed", "Curried", "Combined with legumes"]

#List of different side dishes 
sides = ["Rice and lentils", "Rice and pink beans", "Vegetable Rice", "Sauteed Macaroni", "Sauteed Sphagetti", "Macaroni Salad",
 "Provision pie", "Macaroni and Cheese pie", "Stuffed Potatoes", "Potato Salad"]



#Function for creating a one day meal plan
class Meal:
    def __init__(self):
        meal_meat = random.choice(meat_kind)
        meal_sides = random.choices((sides), k=2)
        meat_prep = random.choice(preparation_method)

        self.meat = meal_meat
        self.prep = meat_prep
        self.sides = meal_sides

    # This returns true if all of the properties are the same
    def compare(self, other_meal):
        if other_meal == None:
            return False
        if other_meal.meat != self.meat:
            return False
        if other_meal.prep != self.prep:
            return False
        if other_meal.sides[0] not in self.sides:
            return False
        if  other_meal.sides[1] not in self.sides:
            return False

    def print(self):
        print(self.meat + " , "+ self.prep + ", " + self.sides[0] + ", " + self.sides[1])

            

def meal_generator(meal_day, num_meals):
    prev_meal = None
    while meal_day <= num_meals:
        
        current_meal = Meal()

        # Comparing the items in currnet meal to the previous meal generated
        if current_meal.compare(prev_meal):
            current_meal = Meal()
            
        #print out results of meal gernerated
        current_meal.print()
        # Updating previous meal for next iteration
        prev_meal = current_meal
        meal_day += 1

    print("Do enjoy your meals.")

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

meal_print()






