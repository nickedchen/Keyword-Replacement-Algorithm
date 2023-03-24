import os
import csv
import time

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
    for review_file in review_files:
        with open(os.path.join(path, review_file), 'rb') as file:
            data = file.read().replace(b'\0', b'')
            reader = csv.DictReader(data.decode('utf-8').splitlines())
            for row in reader:
                if row['content']:
                    review_list.append(row['content'])
    return review_list


#Replaces all acronyms with their expansions in the list of reviews
def replace_acronyms(reviews, acronym_list, expansion_list):
    modified_reviews = []
    for review in reviews:
        words = review.split()
        for i, word in enumerate(words):
            word = word.lower()
            if word in acronym_list:
                index = acronym_list.index(word)
                words[i] = expansion_list[index]
        new_review = " ".join(words)
        modified_reviews.append(new_review)
    return modified_reviews


def test1(review_list, acronym_list, expansion_list):
    start_time = time.perf_counter()
    modified_reviews = replace_acronyms(review_list, acronym_list, expansion_list)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    test_review_list = ["I will be right back", "shaking my head got to go no problem", "shaking my head got to go no problem"]
    test_result = "Fail"
    if modified_reviews == test_review_list:
        test_result = "Success"
    return modified_reviews, execution_time, test_result


def test2(review_list, acronym_list, expansion_list):
    start_time = time.perf_counter()
    modified_reviews = replace_acronyms(review_list, acronym_list, expansion_list)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    review_count = len(modified_reviews)
    test_result = "Fail"
    if review_count == len(review_list):
        test_result = "Success"
    return review_count, execution_time, test_result

