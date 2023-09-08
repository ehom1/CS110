import random

# Part A
weeks = 16
print(weeks, type(weeks)) #weeks
classes = 5
print(classes, type(classes)) #classes
tuition = 6000
print(tuition, type(tuition)) #tuition
cost_per_week = (tuition / classes) / weeks
print(cost_per_week, type(cost_per_week)) #cost per week
print("Cost per week:", cost_per_week)

classes_per_week = 4
print(classes_per_week, type(classes_per_week)) #classes per week
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class)) #cost per class
print("Cost per class:", cost_per_class)

#Part B
list = ["chicken", "cow", "pig", "sheep", "lamb"]
rand = random.choice(list)
print("Random data object from list:", rand)