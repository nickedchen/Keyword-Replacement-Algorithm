import os
import csv
import time

acronymList = []
expansionList = []
reviewList = []

#Stores all acronyms and expansions into their own lists
def load_acronyms(path):
    acronym_list = []
    expansion_list = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            acronym_list.append(row['acronym'])
            expansion_list.append(row['expansion'])
    return acronym_list, expansion_list


#Stores all reviews from all review files into a list
def load_reviews(path):
    review_list = []
    review_files = os.listdir(path)
    for file in review_files:
        with open(os.path.join(path, file), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['content']:
                    review_list.append(row['content'])
    return review_list

#current issues: 
#words only get replaced if there is a space right before and after it. cannot end with period or comma
#some acronyms have multiple expansions and the first one in the expansion list is always used
def replace_acronyms(reviews, acronym_list, expansion_list):
    replaced_reviews = []
    for review in reviews:
        words = review.split()
        for i, word in enumerate(words):
            if word in acronym_list:
                index = acronym_list.index(word)
                words[i] = expansion_list[index]
        new_review = " ".join(words)
        replaced_reviews.append(new_review)
    return replaced_reviews


#temporary test
print(reviewList)
startTime = time.perf_counter()
replacedReviews = Algorithm1(reviewList, acronymList, expansionList)
endTime = time.perf_counter()
print(replacedReviews)
print(f"Algorithm 1 execution time: {endTime - startTime:.2f} seconds")