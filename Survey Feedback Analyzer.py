# Survey Feedback Analyzer

# Step 1: Given Feedback Data

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj','Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks

n = int(input("How many feedbacks do you want to add? "))

for i in range(n):

    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Clean the Feedbacks


for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    feedback = " ".join(feedback.split())

    feedback = feedback.lower()

    feedback_data['Feedback'][i] = feedback

# Step 4: Count Good, Poor and Excellent

def count_words():

    good = 0
    poor = 0
    excellent = 0

    for feedback in feedback_data['Feedback']:

        if "good" in feedback.split():
            good = good + 1

        if "poor" in feedback.split():
            poor = poor + 1

        if "excellent" in feedback.split():
            excellent = excellent + 1

    print("\nWord Count")
    print("Good:", good)
    print("Poor:", poor)
    print("Excellent:", excellent)


count_words()


# Step 5: Average Rating

def average_rating():

    total = sum(feedback_data['Rating'])

    average = total / len(feedback_data['Rating'])

    print("\nAverage Rating:", average)


average_rating()


# Step 6: Find Longest Feedback

longest_feedback = ""
max_words = 0

for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())

    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback

print("Longest Feedback:", longest_feedback)
print("Number of Words:", max_words)



# Step 7: Find Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:
    words = feedback.split()

    for word in words:
        unique_words.add(word)

print("Unique Words:", list(unique_words))

# Final Cleaned Data

print("\nFinal Cleaned Feedback Data:")
print(feedback_data)
