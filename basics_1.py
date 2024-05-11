#my_dic = {"key1":"value1", "key2":"value2", "key3":"value3"}
#print(my_dic["key1"])

#prices_lookup={"apple":"2.99", "oranges":"1.99", "milk":"5.80"}
#print(prices_lookup["oranges"])

#set("Mississippi")

##############################
#myfile = open("test.txt")
#print(myfile.read())


#myfile = myfile.readlines()
#print(myfile)
#for line in myfile:
#  print(line)
###########################

#with open("test.txt") as my_new_file:
#  contents = my_new_file.read()

#  print(contents)

######################

#with open ("romeo_y_julierta.txt", mode = "r") as f:
  #print(f.read())


#with open ("romeo_y_julierta.txt", mode = "a") as f:
  #print(f.write("\nJULIETA\n¡Mil veces buenas noches!"))

#with open ("romeo_y_julierta.txt", mode = "r") as f:
#  print(f.read())

################write lines in code#####################

#with open ("romeo_y_julieta_2.txt", mode = "w") as f2:
#  f2.write("\nJULIETA\n ¡Chss, Romeo, chss! ¡Ah, quién fuera cetrero\npor llamar a este halcón peregrino!\nMas el cautivo habla bajo, no puede gritar;\nsi no, yo haría estallar la cueva de Eco\ny dejaría su voz más ronca que la mía\nrepitiendo el nombre de Romeo\n")


#with open ("romeo_y_julieta_2.txt", mode = "r") as f2:
#  print(f2.read())
####################FIND PRIME NUMBERS###########

#nlist = list(range(0))
#super_list=[]
#prime_number=[]
#x=0
#for n in nlist:
#  new_list =nlist 
#  for m in new_list:
#    if n%m == 0:
#      super_list.append(n)
#for ele in super_list:
#  if super_list.count(ele) == 2:
#    prime_number.append(ele)

#prime_numbers =set()
#for prime in prime_number:
#  prime_numbers.add(prime)
#print(prime_numbers)


############while and else######

#nlist = list(range(1,101))
#super_list=[]
#prime_number=[]
#x=0
#while x < 15:
  
#for n in nlist:
    
#new_list =nlist 
#for m in new_list:
#if n%m == 0:
#super_list.append(n)

#for ele in super_list:
#if super_list.count(ele) == 2:
#prime_number.append(ele)
#x +=1
#print(x)

#else:
#print("stop here")
  
#prime_numbers =set()
#for prime in prime_number:
#prime_numbers.add(prime)
#print(prime_numbers)
  
###############Guessing a prime number#########

#nlist = list(range(1,200))
#super_list=[]
#prime_number=[]
#for n in nlist:
#  new_list =nlist 
#  for m in new_list:
#    if n%m == 0:
#      super_list.append(n)
#for ele in super_list:
#  if super_list.count(ele) == 2:
#    if ele == 43:
#      continue
#    #elif ele == 31:
#      #break
#    else:
#      prime_number.append(ele)

#prime_numbers =set()
#for prime in prime_number:
#  prime_numbers.add(prime)
#print(prime_numbers)

#result = input("Guess a prime number: ")
#if int(result) in prime_numbers:
#  print("You are right!")
  #print(prime_numbers)
#else:
  #print("Try next time")







#string = "Print only the words that start with a letter s in this sentence"

#mystring = string.split()
##print(mystring)


#for letter in mystring:
#  if letter[0] == "s":
#    print(letter)


nlist = list(range(1,101))

for num in nlist:
  if num%15==0:
    print(f"FizzBuzz {num}")
    continue
  if num%3==0:
    print(f"Fizz {num}")
    continue
  if num%5==0:
    print(f"Buzz {num}")
    continue
  #else:
  #  print(f"good {num}")