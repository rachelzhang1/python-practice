points = [[-100, -50], [0, 100], [100, -50]]

#print my_points[0][0], my_points[0][1], my_points[2][0], my_points[1][1]
#print my_points[0], my_points[1], my_points[2], my_points[1][1]

def  get_mid(p1, p2):
	return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

#print get_mid(points[0], points[1])
print points[0], get_mid(points[0], points[1]),get_mid(points[1], points[1])
print points[1], get_mid(points[0], points[1]),get_mid(points[1], points[2])
print points[2], get_mid(points[2], points[1]),get_mid(points[0], points[2])
