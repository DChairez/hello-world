red = int(input())
green = int(input())
blue = int(input())

if (red < green) and (red < blue):
    gray = red
elif (green < red) and (green < blue):
    gray = green
elif (blue < red) and (blue < green):
    gray = blue
else:
    gray = red

red2 = (red - gray)
green2 = (green - gray)
blue2 = (blue - gray)

print (red2, green2, blue2)