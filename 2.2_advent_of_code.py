product_id_list = [12077,25471,4343258,4520548,53,81,43661,93348,6077,11830,2121124544,2121279534,631383,666113,5204516,5270916,411268,591930,783,1147,7575717634,7575795422,8613757494,8613800013,4,19,573518173,573624458,134794,312366,18345305,18402485,109442,132958,59361146,59451093,1171,2793,736409,927243,27424,41933,93,216,22119318,22282041,2854,4778,318142,398442,9477235089,9477417488,679497,734823,28,49,968753,1053291,267179606,267355722,326,780,1533294120,1533349219]
total_id_number = 0

#print("Length of current list:" , len(product_id_list))
for index_of_current_list_num in range(0 , len(product_id_list) , 2):
    #print("Index of current list number:" , index_of_current_list_num)
    for number_in_range in range(product_id_list[index_of_current_list_num] , product_id_list[index_of_current_list_num + 1] + 1): #iterating through ints in the list's ranges, stopping at the final int value in the final range.
        
        if ((len(str(number_in_range)) % 2 == 1) and (len(str(number_in_range)) > 1)): #odd number function
            all_digits_match = True

            for index in range(len(str(number_in_range)) - 1): #odd identical digit tester
                if str(number_in_range)[index] != str(number_in_range)[index + 1]: #check if the digit doesnt match the next digit
                    all_digits_match = False
                    break #if any two digits dont match, stop checking. 
                
            if all_digits_match == True:
                total_id_number += number_in_range #all the digits matched
                print("Invalid odd:" , number_in_range)

            elif len(str(number_in_range)) == 9: #invalid 9 digit tester
                if (str(number_in_range)[:3] == str(number_in_range)[3:6] and str(number_in_range)[3:6] == str(number_in_range)[6:9]):
                    total_id_number += number_in_range #all the digits matched
                    print("Invalid 9 digit specialty odd:" , number_in_range)

        elif (number_in_range // (10 ** (len(str(number_in_range)) // 2)) == number_in_range % (10 ** (len(str(number_in_range)) // 2))): #even digit number, with first half matching the last half
            total_id_number += number_in_range
            #print("Invalid even, first half matches last half:" , number_in_range)

        elif (len(str(number_in_range)) == 6): #invalid 6 digit specialty tester
            if (str(number_in_range)[:2] == str(number_in_range)[2:4] and str(number_in_range)[2:4] == str(number_in_range)[4:6]):
                    total_id_number += number_in_range #all the digits matched
                    print("Invalid 6 digit specialty even:" , number_in_range)
        
        elif (len(str(number_in_range)) == 10): #invalid 10 digit specialty tester
            if (str(number_in_range)[:2] == str(number_in_range)[2:4] and str(number_in_range)[2:4] == str(number_in_range)[4:6] and str(number_in_range)[4:6] == str(number_in_range)[6:8] and str(number_in_range)[6:8] == str(number_in_range)[8:10]):
                    total_id_number += number_in_range #all the digits matched
                    print("Invalid 10 digit specialty even:" , number_in_range)

print(total_id_number)
