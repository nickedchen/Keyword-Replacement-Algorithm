import os
import csv
import time

acronymList = []
expansionList = []
reviewList = []

#Stores all acronyms and expansions into their own lists
directory = os.path.dirname(__file__)
with open(os.path.join(directory, 'data/acronyms/slang.csv'), 'r') as filepath:
    reader = csv.DictReader(filepath)
    for col in reader:
        acronymList.append(col['acronym'])
        expansionList.append(col['expansion'])


#Stores all reviews from all review files into a list
path = os.path.join(directory, 'data', 'testReviews')
reviewFiles = os.listdir(path)
for file in reviewFiles:
    filepath = os.path.join(path, file)
    with open(filepath, 'rb') as filepath:
        data = filepath.read().replace(b'\0', b'')
        reader = csv.DictReader(data.decode('utf-8').splitlines())
        for col in reader:
            if(col['content']):
                reviewList.append(col['content'])

#current issues: 
#words only get replaced if there is a space right before and after it. cannot end with period or comma
#some acronyms have multiple expansions and the first one in the expansion list is always used
def Algorithm1(reviews, acronyms, expansions):
    replacedReviews = []
    for i in range(0, len(reviews)):
        words = reviews[i].split()
        for j in range(0, len(words)):
            for k in range(0, len(acronyms)):
                if(words[j] == acronyms[k]):
                    words[j] = expansions[k]
        newReview = " ".join(words)
        replacedReviews.append(newReview)
    return replacedReviews


#temporary test
print(reviewList)
startTime = time.perf_counter()
replacedReviews = Algorithm1(reviewList, acronymList, expansionList)
endTime = time.perf_counter()
print(replacedReviews)
print(f"Algorithm 1 execution time: {endTime - startTime:.2f} seconds")