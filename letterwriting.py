# Name = input("Please enter your name: ")


# print ("Good Morning" ,Name)
# date = input("enter the date:")
# Name = input ("plz enter the name : ")
# print ( '''Dear''',Name, ''' \nYou are selected!\n''', date)





letter= '''Dear <|NAME|>,
Greetings from youtube . We are happy 
to teel you that you are the best youtuber of india.
Have a great day ahead,
Thanks and regards
Date : <|DATE|>'''

name = input("Enter your Name\n")
date = input ("Enter Date \n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print (letter)
# Write a program to detect double spaces in a string.

# story = '''I hope not.   You might pull a muscle.

# You need to start small in   order to achieve something big like that.

# When it comes to learning English,   what if I told you that you can understand big ideas with just a little bit of text?

# You do not need to wait several    years to deal with complex ideas.

# Just because you are learning a language does not mean you need to limit your thinking.'''


# print (story.find('  '))

# print (story.replace("  "," "))



