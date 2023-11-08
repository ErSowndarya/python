#if statement is true, does not go to the next line(ELIF)

light="red"
if light=="red":
#red==red(true so print result is blue)
    light="blue"
elif light=="blue":
    light="red"
print(light)