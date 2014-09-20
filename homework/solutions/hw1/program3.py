'''
Your manager orders Austin's Pizza every Friday for you and your fellow
coworkers. You're getting tired of figuring out how many pizzas you need to
buy, so you decide to automate the process. You're also getting tired of
Austin's Pizza and would prefer East Side Pies, but complaining about free
food doesn't set you up well for a promotion. Create a program which lets the
user input the number of people eating, the number of slices each will eat,
and the number of slices per box of pizza. The program should print out the
minimum number of pizza boxes necessary to feed the office based on the values
provided.
'''

num_people = int(raw_input("How many people are eating today: "))
slices_per_person = int(raw_input("How many slices will each person eat: "))
slices_per_box = int(raw_input("How many slices does each box contain: "))

total_slices_needed = num_people * slices_per_person

# STRATEGY 1
# We use float here to avoid integer division: we need to see if there will be
# a remainder at the end of the division. This is important, because we can't
# buy "fractions" of a pizza. If the calculation shows we need 2.1 boxes of
# pizza, that means we actually need 3 boxes.
boxes_needed = float(total_slices_needed) / slices_per_box

# We can borrow our solution from program #2 to determine if the number of boxes
# needed is a whole number. If it's a whole number, we can leave it as is.
# Otherwise, we must add a box of pizza to account for the "fractional" pizza
# necessary to feed everyone.
if boxes_needed != int(boxes_needed):
    boxes_needed += 1

print("You will need %d boxes of pizza" % boxes_needed)

# STRATEGY 2
# We can keep boxes_needed as an integer and use modular arithmetic to determine
# if the boxes needed evenly divides the total slices needed. For two integers a
# and b, if a%b == 0, then we can conclude b divides a evenly. Examples:
# >>> 10%5
# 0
# >>> 9.0%3
# 0.0
# >>> 15%4
# 3
# If the slices per box doesn't evenly divide the total slices, then there will
# be a remainder, meaning we need to add a box.
boxes_needed = total_slices_needed / slices_per_box

if (total_slices_needed % slices_per_box != 0):
    boxes_needed += 1

print("You will need %d boxes of pizza" % boxes_needed)
