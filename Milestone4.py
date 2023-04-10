import os
import csv
import time

def load_acronyms(path):
    acronym_expansion_map = {}
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            acronym = row['acronym']
            expansion = row['expansion']
            acronym_expansion_map[acronym] = expansion
    return acronym_expansion_map

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

def replace_acronyms(reviews, acronym_expansion_map):
    modified_reviews = []
    for review in reviews:
        words = review.split()
        for i, word in enumerate(words):
            word = word.lower()
            if word in acronym_expansion_map:
                words[i] = acronym_expansion_map[word]
        new_review = " ".join(words)
        modified_reviews.append(new_review)
    return modified_reviews


def test1(review_list, acronym_expansion_map):
    start_time = time.perf_counter()
    modified_reviews = replace_acronyms(review_list, acronym_expansion_map)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    test_review_list = ["I will be right back", "shaking my head got to go no problem", "shaking my head got to go no problem"]
    test_result = "Fail"
    if modified_reviews == test_review_list:
        test_result = "Success"
    return modified_reviews, execution_time, test_result


def test2(review_list, acronym_expansion_map):
    start_time = time.perf_counter()
    modified_reviews = replace_acronyms(review_list, acronym_expansion_map)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    review_count = len(modified_reviews)
    test_result = "Fail"
    if review_count == len(review_list):
        test_result = "Success"
    return review_count, execution_time, test_result