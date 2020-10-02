from random import choice
#adding a library for the random funtion

def get_file_lines(filename):
    infile = open(filename, "r")
    lines_list = infile.readlines()
    infile.close()
    return lines_list  

line_list = get_file_lines("poem.txt")
#line-list is the poem file and lines of the poem
print(get_file_lines("poem.txt"))
print(line_list)

def lines_printed_backwards(lines_list):  
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_number = lines_length - i
        print(f"{line_number} {line}")
lines_list = get_file_lines("poem.txt")
lines_printed_backwards(lines_list)       


def lines_printed_random(lines_list):
    for i in range(len(lines_list)):
        print(choice(lines_list))

lines_printed_random(line_list)
        

def lines_printed_custom(lines_list): 
    for line in lines_list:    
        words = line.split(" ")  
        print(words[0])


lines_printed_custom(line_list)
#worked with Sawyer, Arjun & Lon


