def coord_input():
    coord_1 = input("Enter the first coordinates (Example: x1,y1): ")
    coord_2 = input("Enter the second coordinates (Example: x2,y2): ")
    coord_1 = coord_1.split(",")
    coord_2 = coord_2.split(",")
    coord = coord_1 + coord_2
    return coord
    
    
def find_slope_b():
    coord = coord_input()
    slope = (int(coord[3])-int(coord[1]))/(int(coord[2])-int(coord[0]))
    b = int(coord[1])-float(slope)*int(coord[0])
    return slope, b

def return_y():
    slope, b = find_slope_b()
    x = int(input("Enter the x-coordinate: "))
    y = slope*x+b
    y_output(y)
    
def y_output(y):
    print("The y-coordinate is {}.".format(y))
    return
  
  
if __name__ == "__main__":
    return_y()