def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        result = 0
        
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            result = element_1 / element_2
            
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result_list.append(result)
    
    return result_list