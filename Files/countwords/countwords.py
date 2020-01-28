"""This program reads a file and counts how many times each word appears in the file."""

import string
import operator

def turn_file_to_string(file_name):
    with open(file_name,'r') as reader:
      # saving the file content in a string
        text_from_file = reader.read()
    # getting rid of punctuation
    exclude = set(string.punctuation)
    text_from_file = ''.join(ch for ch in text_from_file if ch not in exclude)   
    # returning a clean, lower case string 
    return text_from_file.lower()
# print(turn_file_to_string('short_story.txt'))

# dict that counts appearences of each word
def create_dict_from_string(str):
  list_of_words = str.split()
  counts_dict = {}
  for word in list_of_words:
    if word not in counts_dict:
      counts_dict[word] = 0
    counts_dict[word] += 1
  return counts_dict

# print(create_dict_from_string(turn_file_to_string('short_story.txt')))

# creating a sorted list from the dictionary
def dict_to_list(dict):
  new_list = []
  for key, value in dict.items():
    temp = [key,value]
    new_list.append(temp)
  # sorting the list alphabetically by first element
  new_list.sort(key = operator.itemgetter(0))
  return new_list
    
print(dict_to_list((create_dict_from_string(turn_file_to_string('short_story.txt')))))