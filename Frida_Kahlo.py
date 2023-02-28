'''
Use your knowledge of Python lists to create a master list of each painting, 
its date, and its audio tour ID.
'''

paintings = ['The two frias', 'My dress hangs here', 'Tree of hope', 'Self portrait with monkeys']
dates = [1939, 1933, 1946, 1940]

#Zip together lists
paintings_zip = zip(paintings, dates)
paintings = list(paintings_zip)

#Appending more shows
paintings.append(['The broken column', 1944])
paintings.append(['The wounded deer', 1946])
paintings.append(['Me and my doll', 1937])

#Length of painting list
paintings_list = len(paintings)

#Generate a list of identification numbers, starting at 1 to length to out list of items
audio_tour_number = range(1,paintings_list)
audio_tour_number_list = list(audio_tour_number)

master_list_zip =  zip(paintings, audio_tour_number)
master_list = list(master_list_zip)

#Printing paintings with its id
print('-------Paintings with its id number--------------')
for i in range(len(master_list)) :
  
  print(f"Painting: {master_list[i][0]} Id: {master_list[i][1]}" )
  
