"""
In front of you are two lists.first belongs to first and so on.
1 ) write a single line of code that creates a list in which every item is the name of a movie and the actress that plays in it:
Gone Girl is played by Rosamund Pike
"""
movie = ['The Notebook', 'Maleficent', 'Batman V Superman', 'Black Swan','Gone Gril', 'war of the Worlds', 'Just Married']

actor = ['Rachel MdAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman', 'Rosamund Pike', 'Dakota Fanning', 'Brittany Murphy']

# ex 2:
movies = { key: value for key, value in zip(movie,actor)}
# print(movies)

# print(["{movie} is played by {actor}".format(movie=movie,actor=actor) for movie, actor in movies])

#ex 3: take the dictionary movies and write a single line of code that represents the same list as ex 1:

# print(["{movie} is played by {actor}".format(movie=movie,actor=actor) for movie, actor in movies.items()])

#ex 4: create a list that includes each number from 1 to 9 (inclusive), multiplied by 100. only imclude the number if its divisible by 2 with no remainder.
""">>> [200, 400, 600, 800] """

# print([i*100 for i in range(10) if i%2==0])

#ex 5: create a list that includes each number from 1 to 9 (inclusive), multiplied by 100, only if its divisible by 2 with no remainder, if theres a remainder, leave the number as is, and dont multiply it by 100.
""">>> [1, 200, 3, 400, 5, 600, 7, 800, 9]"""
# print([i*100 if i%2==0 else i*1 for i in range(1,10)])

# ex 6: write code that creates a list that displays the numbers between 1 and 99. if the number is divisible by 7 with no remainder, replace it with the string "BOOM"

# print(["BOOM" if i%7 == 0 else i for i in range(1,100)])
print(map(lambda x: "BOOM" if x%7 ==0 else x, range(1,100)))

#ex 7: write a single line of code, named sum that recieves 2 numbers and returns the sum.
# sum(3,4) >>> 7

sum = lambda x,y : x + y
# print(sum(3,4))

#ex 8 : write a single line of code that creates a list of tuples of all 36 different combinations of (1,1) to (6,6)
# print([(i,j) for i in range(1,7) for j in range(1,7)])

#ex 9: convert joules to kilocalories by dividing the number of joules by 4184.
# write a single line of code that creates  list of tuples where the first item in each tuple is the energy in houles and the second is in kilocals. 
joules = [5000.0, 8000.0, 10000.0, 6000.0, 12000.0]
# print([zip(joules,("{:.9f}".format(i/4184.0) for i in joules))])
# print(list((j,cal) for (j,cal) in zip(joules,map(lambda i: i/4184, joules))))

#ex 10: using filter and lambda write code that returns a list that contains only the language that you know.
languages = ["HTML", "JavaScript", "Python", "Ruby"]
# print(filter(lambda i : i == "Python", languages))
#convert:
# print([x for x in languages if x== "Python"])