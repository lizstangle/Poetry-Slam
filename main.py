def get_file_lines(filename):
    infile = open(filename, "r")
    lines_list = infile.readlines()
    infile.close()
    return lines_list  

    # print(get_file_lines("poem.txt"))

def lines_printed_backwards(lines_list):  
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_list):
        line = lines_list[i]
        line_number = lines_length - i
        print(f"{line_number} {line}")

from random import choice

def lines_printed_random(lines_list):
        for line in lines_lists:
            print(choice(lines_list))

def lines_printed_custom(lines_list):   
    lines_lenth = lin(lines_list)





#     lines_printed_backwards(lines_list):     
#     lines_list.reverse()     lines_length = len(lines_list)     for i in range(lines_list):         line = lines_list[i]         line_number = lines_length - i         print(f"{line_number} {line}") 

# #     or 
# #     for line in infile:
# #         print(line)
# #     result = 

# # def lines_printed_backwards(lines_list):  
# #     print(lines_list).reverse

# # from random import choice
# # def lines_printed_random(lines_list):
# #     number_lines = len(poem)
# #     random.randint(0, len(locations))


# #     def lines_

# # def lines_printed_customer(lines_list)




# def lines_printed_custom(lines_list):
#     lines_length = len(lines_list)

#     for i in range(lines_list):
#         if i % 4 == 0 and i % 2 ==0:
#             print(lines_length[i])
    