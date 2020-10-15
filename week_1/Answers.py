#1. Generate all Prime numbers between 0 and 100

def primes_method(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

print(primes_method(100))

#2. Order the list ['banana', 'apple', 'zebra', 'raspberry'] in alphabetical order
list = ['banana', 'apple', 'zebra', 'raspberry']

list.sort()

print(list)

#3. Generate 2 sets of numbers and determine which numbers are common to both sets.
import random

# Generate 10 random numbers between 1 and 100

A = random.sample(range(0, 100), 10)
B = random.sample(range(0, 100), 10)

print(set(A).intersection(set(B)))

#4. Make a dictionary of people you know with their birthdays. Write a function which takes the names of any two people and return the difference between their birthdays in minutes.
import datetime

dict = {'Mike' : datetime.datetime(1995, 5, 16),
 'John': datetime.datetime(1993, 7, 28), 
 'Roxanne' : datetime.datetime(1997, 3, 7)}

def diff_in_minutes(name1, name2, input_dictionary = dict):
 	diff = abs(input_dictionary[name1] - input_dictionary[name2])
 	minutes_diff = diff.days * 24 * 60

 	return minutes_diff

# Example
print(diff_in_minutes(name1 = 'Roxanne', name2 = 'John', input_dictionary = dict))

#5. Make a .txt file in your computer, make every odd numbered sentence in uppercase and every even sentence lowercase. Save this via Python as a new text file in the same directory as the old file. 
# Read in file
f = open("sample_txt_file.txt", "r")
sample_txt_file = f.read()

# Separate into sentences
from nltk import tokenize
sentences = tokenize.sent_tokenize(sample_txt_file)

# Set odd numbered sentences as uppercase and even numbered sentences as lowercase
output_sentences = []

for i in range(0, len(sentences)): 
	if i % 2 == 0:
		def transform(x):
			y = x.upper()
			return y
	else: 
		def transform(x):
			y = x.lower()
			return y
	output_sentences.append(transform(sentences[i]))

# Make into a single string
joined_sentences = ' '.join(output_sentences)

# Write to a txt file
f = open("transformed_txt_file.txt", "w")
f.write(joined_sentences)
f.close()

#6. Given a list of numbers [38, 42, 53, 94, 1, 3, 4, 79] and return an indicator flag list where 1 indicates if the number is even. Answer should be [1, 1, 0, 1, 0, 0, 1, 0].
lst = [38, 42, 53, 94, 1, 3, 4, 79]

indicator_lst = [1 if i % 2 == 0 else 0 for i in lst]

print(indicator_lst)

#7. Count words in a string
string = ['this is a string', 'this is another string']

print([len(i.split()) for i in string])

#8. Count how many times each value is in a list.
items = ['apple', 'banana', 'carrot', 'apple', 'banana', 'apple']
itemset = list(set(items))
itemset.sort()

item_count = []
for i in range(0, len(itemset)):
	current_item_count = items.count(itemset[i])
	item_count.append(current_item_count)

item_dict = dict(zip(itemset, item_count))

print(item_dict)

#9. Given a list, return a deduped list while maintaining its order.

duped_list = [1, 50, 2, 2, 3, 3, 3, 4, 4, 4, 4, 6, 6, 5, 5, 5]

deduped_list = []

for i in range(0, len(duped_list)):
	candidate_element = duped_list[i]
	if (deduped_list.count(candidate_element) == 0):
		deduped_list.append(candidate_element)
	else: 
		deduped_list = deduped_list

print(deduped_list)












