import random
random.seed(42)

possible_scores = list(range(1,11))
score_list1 = random.choices(possible_scores, weights=[8,8,8,8,8,3,3,4,20,30], k=10)
score_list2 = random.choices(possible_scores, weights=[1,2,3,4,5,10,15,15,7,9], k=450)
score_list3 = random.choices(possible_scores, weights=[1,2,3,4,4,5,5,10,15,25], k=10000)

negative =[]
neutral = []
positive = []

def score_counter(score_list):
    for score in score_list:
        if score in range(1,6):
            negative.append(score)
        elif score in range(6,9):
            neutral.append(score)
        elif score in range(9,11):
            positive.append(score)
            
    print('Negative: ' + str(len(negative)))
    print('Neutral: ' + str(len(neutral)))
    print('Positive: ' + str(len(positive)))
    
    
#score_counter([1,2,3,4,5,6,7,8,9,10])
score_counter(score_list3)
