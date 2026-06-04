product_id_list = [12077,25471,4343258,4520548,53,81,43661,93348,6077,11830,2121124544,2121279534,631383,666113,5204516,5270916,411268,591930,783,1147,7575717634,7575795422,8613757494,8613800013,4,19,573518173,573624458,134794,312366,18345305,18402485,109442,132958,59361146,59451093,1171,2793,736409,927243,27424,41933,93,216,22119318,22282041,2854,4778,318142,398442,9477235089,9477417488,679497,734823,28,49,968753,1053291,267179606,267355722,326,780,1533294120,1533349219]
total_id_number = 0

print("Length of current list:" , len(product_id_list))
for index_of_current_list_num in range(0 , len(product_id_list) , 2):
    print("Index of current list number:" , index_of_current_list_num)
    for number_in_range in range(product_id_list[index_of_current_list_num] , product_id_list[index_of_current_list_num + 1] + 1):
        if (len(str(number_in_range)) % 2 == 1):
            continue
        elif (number_in_range // (10 ** (len(str(number_in_range)) // 2)) == number_in_range % (10 ** (len(str(number_in_range)) // 2))):
            print(number_in_range)
            total_id_number += number_in_range
print(total_id_number)
