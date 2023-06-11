''' question
Imagine working on software that deals with restaurant reviews.

Create a function named get_highest_rated that is responsible for finding the highest-rated restaurant.

This function should take in a list of dictionaries named restaurants as a parameter. Each dictionary represents the data associated with a restaurant, including its rating. This function should have a return value of the restaurant with the highest rating.
'''

''' feedback
Great job! Short, sweet, easy to read!

Let's move lines 5-6 up at the top first (this is common practice to put these "guard clauses" at the top), so that we don't create variables that might be thrown out right after.

Also, we have the rating already inside highest_restaurant, so how might we use that rather than a second variable?
'''

def get_highest_rated(restaurants):
    if not restaurants:
        return None
    
    highest_restaurant = {}
    highest_rating = 0
        
    for restaurant in restaurants:
        if restaurant["rating"] > highest_rating:
            highest_restaurant = restaurant
            highest_rating = restaurant["rating"]
            
    return highest_restaurant