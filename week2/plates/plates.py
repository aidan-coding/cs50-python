def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    Valid = 0 
    #Valid if meets all 7 requirments


    if len(s) <= 7: # checks if more than 6
        Valid += 1

    if len(s) >= 3: #  checks if less than 2
        Valid += 1

    if s[0:2].isalpha: # checks if first 2 char is letters
        Valid += 1

    space = " " in s # checks if any spaces
    if space == False:
        Valid += 1
    count = 0
    
    for i in s: # checks if any punctuation marks
        if i not in "'.!?,":
            count += 0
        else: count += 1
        if count > 0:
            break
    if count == 0:
        Valid += 1

    #check if first number isn't 0
    if "0" in s:
        find_0 = s.index("0")
        if s[:find_0].isalpha():
            pass
        else:
            Valid += 1
    else:
        Valid += 1

    
    num = 0
    not_let = 0
    
    while num == 0: #check if nums at the end
        if s[not_let].isalpha == True:
            not_let += 1
            continue
        else: 
            num = 1
            not_let += 2
        if num == 1:
            if s[not_let:].isdigit:
                Valid += 1
    if num == 0:
        Valid += 1
        
    first_num_found = False
    num_location = 0
    for char in s:
        if char.isdigit():
            first_num_found = True
            break
        else:
            num_location += 1

    all_nums = s[num_location:]
    if all_nums.isdigit() == True:
        Valid += 1
    if first_num_found == False:
        Valid += 1
    


    if Valid == 8:
        return True



    


        
    

main()