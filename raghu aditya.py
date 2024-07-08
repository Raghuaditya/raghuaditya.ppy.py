# Define the quiz questions and answers
quiz = [
    {
        "question": "What is the capital of jammu and kasmir?",
        "options": ["A. srinagar", "B. London", "C. jammu", "D. kashmir"],
        "answer": "A"
    },
    {
        "question": "What is the tenure of indian prime minister?",
        "options": ["A. 3 years", "B. 4 years", "C. 5 years", "D. 6years"],
        "answer": "c"
    },
    {
        "question": "Who wrote 'Micrographia'?",
        "options": ["A. robert hooke", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol of nitrogen oxide?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. N2"],
        "answer": "D"
    },
    {
        "question": "Who is the painter among the following?",
        "options": ["A. Charles Babbage", "B. Rudolf Virchow", "C. Leonardo da Vinci", "D. Camillo Golgi"],
        "answer": "C"
    }
]

# Function to conduct the quiz
def conduct_quiz(quiz):
    score = 0
    for i, item in enumerate(quiz):
        print(f"Question {i+1}: {item['question']}")
        for option in item["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == item["answer"]:
            score += 1
        print()  # Newline for better readability

    print(f"You got {score} out of {len(quiz)} questions correct!")

# Start the quiz
conduct_quiz(quiz)