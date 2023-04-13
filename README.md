# Keyword Replacement Algorithm

> An algorithm to replace abbreviations in a given text review with their expanded forms. 



The repository includes two versions of the same algorithm. Both implementations of the algorithm take a text string as input and return a new string with the abbreviations replaced by their expanded forms. The input text and the dictionary of abbreviations and their expansions are provided as arguments to the function.

## Datasets

The algorithm was tested against with the reviews dataset provided by the course instructor Dr. Fard and Acronyms dataset provided by [Kaggle](https://www.kaggle.com/datasets/gowrishankarp/chat-slang-abbreviations-acronyms).

## Implementation

The first implementation, milestone 3, was created using brute force method with two for loops. The first for loop iterates through each review and splits the review into a list of words. The second for loop iterates through each word and converts it to lower case, and then checks to see if it is in the acronyms list. If it is, the word gets replaced with the expansion corresponding to the acronym. The function finishes by returning the new review list containing the expansions instead of acronyms. 


``` python
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

```

The second algorithm utilizes hashmap to reduce the time complexity. The main modification made in the second algorithm was the use of a hashmap to store the acronyms and their corresponding expansions, instead of a list of tuples as used in the first algorithm. This allowed for constant time lookup of the expansion for each acronym, resulting in a significant reduction in the time complexity of the function. The load_acronyms function was modified to read the data and store it as a dictionary, with the acronyms as the keys and their expansions as the values.

``` python

def replace_abbreviations(M, H): # M is the input string, H is the hashmap dataset        
M_splited = M.split() # Split the message into words
    	for i in range(len(M_splited)):
        # Check if the word is an abbreviation in the hashmap
        if M_splited[i].lower() in H:
            # Replace the abbreviation with its full form
            M_splited[i] = H[M_splited[i].lower()]
    # Join the modified words back into a single string
    M_prime = ' '.join(M_splited)
    # Return the modified message
    return M_prime
```    

## Results
The time complexity of our second algorithm is O(n), where n is the number of words in all the reviews combined. As shown in the plot below, our algorithm's execution time increases at nearly the same rate as the expected time, making it just as effective as we expected it to be. Our choice of using a hashmap as our data structure had a massive impact on the performance of the algorithm. It reduced our first algorithm’s time complexity of O(nm) to O(n) because of the hashmaps' nearly instant lookup time of acronyms. The use of a hashmap resulted in the algorithm executing roughly 158 times faster than the original algorithm.

<img width="424" alt="image" src="https://user-images.githubusercontent.com/88886207/231655091-c8d5a380-7299-43c1-993a-cdc044514c41.png">

## Conclusion
Our improved version of the algorithm provides a more efficient and accurate solution to the acronym expansion problem in text reviews. It executes roughly 158 times faster than the original algorithm, and has a time complexity of O(n), where n is the number of words in all the reviews combined. This makes it scalable and suitable for large datasets.
