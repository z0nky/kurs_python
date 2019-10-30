# tak można zaimportować modu i go używać, ale oczywiście można pominąć pisanie "t."
import triangle

print(triangle.a)
print(triangle.h)

print(triangle.triangle_area(4, 8))

# a tak można pominąć "t.":

#from triangle import triangle_area, a, h # triangle_area as tf zaimportuje z funkcje z aliasem
#from triangle import * # import WSZYSTKIEGO
#
#print(a)
#print(h)
#
#area = triangle_area(4, 8)
#print(area)
