
#prime numbers finder

prime_numbers_list = []
all_inputs_list = []
division_list = [2,3,5,7]

counter=1
input_number=1

#Check whether the number is prime or not
def prime_number_check(x):
    prime_counter=0
    for y in division_list:
        #Prime numbers are divided to `1` and itself only. So here input is divided to each member of division_list  
        if not (x%y==0):
            prime_counter+=1
        if (prime_counter==4) or (x==y):
            if not (x==1):
                prime_numbers_list.append(x) 
    

while int(input_number) !=0 and counter<=20:
    input_number=input("Please enter a number:")
    #request input till a digit entered
    while not input_number.isdigit():
        input_number=input("Input is NOT a number. Please enter a number:")
        
    all_inputs_list.append(str(input_number))
    prime_number_check (int(input_number))
    counter+=1

            

print ("All numbers given:", all_inputs_list)
print ("Prime numbers in given numbers:", prime_numbers_list)
sorted_listed= sorted (prime_numbers_list)
print ("Sorted prime numbers in given numbers:", sorted_listed)
 

