# A calculator for the total number of filled boxes and loose notebooks

n = int(input("Total Number of Notebooks:"))
t = int(input("How many notebooks fit in one box:"))

full_boxes = n//t # Gives the total number of full boxes
loose_notebooks = n%t # Gives the total number of loose notebooks

print ("There are", full_boxes, "full boxes")
print ("There are", loose_notebooks, "loose notebooks")

# A conditional statement added when the number of notebooks is less than the box's capacity. 
if n<t:
    print ("no full box was filled.")
