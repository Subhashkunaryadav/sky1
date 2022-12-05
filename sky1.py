print ("Hello World")
message = ('Hi myself subhash kumar yadav and i am pursuing bca and want to do job\n thn this is the things which makes well !')
print (message)

#variables
message = ('This is my message')
print (message)

#string
string1 = ("This is string")
string = ('This is also string')
print (string1)

name = "subhash kumar yadav"
first_name = "subash"
last_name = "yadav"
full_name = first_name+" "+last_name 
print (" Hello " + full_name)
print (name.upper())
print (name.lower())


message = ( "hello this is the string and also these are the subjects studied;\n\tBCA\n\tMCA\n\tBCOM")
print (message)

#numbers
print ( 5 + 3 )
print (5-4)
print (5+1)
print (5**2)
print ((2+3)*4)
print (0.1 + 0.1)
print (1.2 + 1.1)
print (1.4*1.3)  

age = 21
message = " happy " + str(age) + "'" +"rd" + " birthday "
print (message)

age = 22
message = " good "+ str(age)+ "'" + "rd" + " birthday "
print (message) 

#lists
cars = ['bmw', 'audi', "benz", 'alto']
print (cars[0])
print (cars[-4])
print  (cars[-2])

motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)

names = ['sky','high','low','middle']
print (names)

names.append('hi') 
print (names)

names.insert(0,'hello')
print (names)

del names[3]
print (names)

del motorcycles[1]
print (motorcycles)

names = ['sky', 'high', 'low', 'middle']
print (names)

popped_names = names.pop()
print(names)
print(popped_names)

guest = ['ram', 'sham', 'lakshman']
print ("Hi you are invited for my dinner party " + guest[0].upper()+".")
print ("Hi you are invited for my dinner party " + guest[1].upper()+".")
print ("Hi you are invited for my dinner party " + guest[2].upper() + ".")
print ("sorry but for this dinner party he cant attend due to some reason "+guest[1].upper()+".")
guest.remove ('sham')
print (guest)
guest.insert (1,'sun')
print (guest)
print ("Hi you are invited for my dinner party " + guest[0].upper()+".")
print ("Hi you are invited for my dinner party " + guest[1].upper()+".")
print ("Hi you are invited for my dinner party " + guest[2].upper() + ".")
print ("As there are many attendance so this night is going to be a bigger dinning table.")
guest.insert (0,'sky')
print (guest)
guest.insert (2, 'dell')
print (guest)
guest.append ('asus')
print (guest)
print ("Hi you are invited for my dinner party " + guest[0].upper()+".")
print ("Hi you are invited for my dinner party " + guest[1].upper()+".")
print ("Hi you are invited for my dinner party " + guest[2].upper() + ".")
print ("Hi you are invited for my dinner party " + guest[3].upper()+".")
print ("Hi you are invited for my dinner party " + guest[4].upper()+".")
print ("Hi you are invited for my dinner party " + guest[5].upper() + ".")

print ("Sorry as the dinning table will no be max because some won't arrive on time for dinner except two so just get ready dinning table for two \n now there is invitition for only 2 people")

guest.remove ('ram')
message= ("sorry ram i can't invite you for the dinner")
print (guest)
print (message)

guest.remove ('sky')
message= ("sorry sky i can't invite you for the dinner")
print (guest)
print (message)

guest.remove ('sun')
message= ("sorry sun i can't invite you for the dinner")
print (guest)
print (message)

guest.remove ('dell')
message= ("sorry dell i can't invite you for the dinner")
print (guest)
print (message)

message = ("lakshman  u  are still in for the dinning table.")
print (message)
message = ("asus u are still in for the dinning table.")
print (message)

del guest [0]
print (guest)

del guest [0]
print (guest)

guest = []
print (guest)




