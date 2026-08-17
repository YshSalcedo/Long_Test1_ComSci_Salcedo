#There are specific scenarios that requires specific handling when standard procedures fail.

n = int(input("Total Number of Notebooks:"))
t = int(input("How many notebooks fit in one box:"))

full_boxes = n//t
loose_notebooks = n%t

print ("There are", full_boxes, "full boxes")
print ("There are", loose_notebooks, "loose notebooks")

if n<t:
    print ("no full box was filled.")
