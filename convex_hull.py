import math
import matplotlib.pyplot as plt

points_2d = []
hull = []
x_values = []
y_values = []
x = []
y = []
sp_min = 0
sp_max = 0


def ccw(a, b, c):  # cross product of two vectors with 1 similar coordinate(x or y) to calculate the angle between them
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) # formula to calculate cross product for 2 2d vectors
    if area < 0:  # cross product is negative -> clockwise turn
        return - 1
    elif area > 0:  # cross product is positive -> counterclockwise turn
        return 1
    else:
        return 0  # cross product is 0 -> zero angle -> collinear vectors


def jarvis_march(dataset_2d, sp):  # sp = starting point of convex hull with smallest x coordinate
    k = 0  # counter for iter
    sp_index = dataset_2d.index(sp)  # index of starting point in order to find the next point in the dataset
    next_p_index = 0 
    hull.append(sp) # insert the starting point in the convex hull
    while True:
        if k == 0:
            next_p = dataset_2d[sp_index + 1]   # in the first iteration we pick the point after the starting point in the dataset
        elif k > 1:
            next_p = dataset_2d[(next_p_index + 1) % len(dataset_2d)]  # each iteration we take the next point in the dataset
            # as a candidate
        for j in dataset_2d:  # we loop through each point in the dataset
            if j == sp:  # if the point j is the starting point then we reset the loop in order for a new point to be picked from the dataset
                continue
            if ccw(sp, j, next_p) == 1 or (ccw(sp, j, next_p) == 0 and (math.dist(sp, j) > math.dist(sp, next_p))):     # calculate the cross product of the two vectors                                                                              # to determine whether the point we examine belongs to the convex hull
               next_p = j  # pick next candidate point
        next_p_index = dataset_2d.index(next_p)  # take index of next point
        sp = dataset_2d[next_p_index]   # use index from above to find the next starting point
        if next_p_index == sp_index:  # check whether the new starting point is same as old starting point(with their indexes and not the actual points)
            break
        hull.append(next_p)  # insert current candidate point into the hull
        k += 1 # increase iterations counter

def quickhull(dataset_2d, sp_min, sp_max):
    hull.append(sp_min)
    hull.append(sp_max)
    

def starting_point():
    file = open('dataset.txt', 'r')  # open textfile containing the dataset
    txt_line = file.readline()  # read the file line by line
    txt_split = txt_line.split()  # split the string read from readline() with respect to whitespace
    if len(txt_split) % 2 == 0:     # check whether the total number of floats is divisible by 2
        for k in range(0, len(txt_split), 2):  # create list of vectors(or 2d-points)
            points_2d.append([float(txt_split[k]), float(txt_split[k + 1])])  #insert 2 values every time into points_2d to form a 2d point
    sp_min = points_2d[0]  # pick starting min value as the x coordinate of the first 2d point
    sp_max = points_2d[1]  # pick starting max value as the x coordinate of the second 2d point
    for j in points_2d:  # loop through the x coordinate of all the points in order to find the smallest x coordinate.
        if j[0] < sp_min[0]:      
            sp_min[0] = j[0]
            st_p_min_index = points_2d.index(j)  # take index of starting point
        elif j[0] == sp_min[0]:
            if(j[1] < sp_min[1]):
                sp_min[0] = j[0]
                st_p_min_index = points_2d.index(j) 
    for j in points_2d:
        if j[0] > sp_max[0]:
            sp_max[0] = j[0]
            st_p_max_index = points_2d.index(j)
        elif j[0] == sp_max[0]:
            if(j[1] > sp_max[1]):
                sp_max[0] = j[0]
                st_p_max_index = points_2d.index(j)
    file.close()
    st_p_min = points_2d[st_p_min_index]  # the point with the smallest x is guaranteed to be part of the convex hull thus we use it as the starting point(Jarvis March, Quickhull)
    st_p_max = points_2d[st_p_max_index]  # the point with the biggest x value is guaranteed to be part of the convex hull thus we use it as starting point(Quickhull)  
    
    return st_p_min, st_p_max

def print_hull(points_2d, hull):
    for i in range(len(points_2d)): 
        plt.scatter(points_2d[i][0], points_2d[i][1])  # plot points in points 2d
    for i in range(len(hull)):
        x_values.append(hull[i][0])     # get x coordinates of points in the hull
        y_values.append(hull[i][1])     # get y coordinates of points in the hull
    x_values.append(x_values[0])        # place x coordinates into x_values list
    y_values.append(y_values[0])        # place y coordinates into y_values list
    plt.plot(x_values, y_values)        # plot convex hull
    plt.xlabel("x values", size=12)     # label x axis as x values
    plt.ylabel("y values", size=12)     # label y axis as y values
    plt.show()                          # show scatter and plot
   
sp_min, sp_max = starting_point()
print(sp_min, sp_max)
# jarvis_march(points_2d, sp_min)
# print_hull(points_2d, hull)