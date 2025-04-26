def run_quiz(auto_answers=None):
    questions = [
        {
            "question": "Q1: When it comes to relationships, do you value social norms and appearances more than deep emotional connection and personal authenticity?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]  # 4 points for "No", 0 points for "Yes"
        },
        {
            "question": "Q2: How often do you find yourself frustrated by behaviors in others that you feel are manipulative or insincere?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 1, 2, 3, 4]  # 0 for "Rarely", 1 for "Sometimes", etc.
        },
        {
            "question": "Q3: When making decisions, do you prefer to rely on logic and factual understanding over following popular trends or emotional comfort?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]  # 4 points for "Yes", 0 points for "No"
        },
        {
            "question": "Q4: In social or professional situations, do you prioritize agreeing with others for the sake of harmony over meaningful dialogue and intellectual honesty?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]  # 4 points for "No", 0 points for "Yes"
        },
        {
            "question": "Q5: How often do you feel that people avoid being direct or honest, instead relying on subtle signals or unspoken communication?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 1, 2, 3, 4]  # 0 for "Rarely", 1 for "Sometimes", etc.
        },
        {
            "question": "Q6: When faced with mainstream beliefs or societal expectations, do you tend to question or reject them if they conflict with your personal values?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]  # 4 points for "Yes", 0 points for "No"
        },
        {
            "question": "Q7: Do you believe romantic relationships should be based on external status or superficial factors rather than mutual respect, truth, and compatibility?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]  # 4 points for "No", 0 points for "Yes"
        },
        {
            "question": "Q8: When choosing your social circle, do you prioritize deep connections and shared values over fitting in with popular groups or trends?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]  # 4 points for "Yes", 0 points for "No"
        },
        {
            "question": "Q9: How often do you prefer things that most people find meaningful or entertaining, rather than feel disconnected or alienated by those things?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [4, 3, 2, 1, 0]  # 4 for "Never", 3 for "Rarely", etc.
        },
        {
            "question": "Q10: Do you value objective truth more than social approval or acceptance?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]  # 4 points for "Yes", 0 points for "No"
        }
    ]

    print("Welcome to the Social Game Typology Test!\n")

    total_points = 0
    max_points = len(questions) * 4  # Total possible points (each question worth 4 points)

    for idx, q in enumerate(questions, 1):
        print(q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"  {i}. {option}")

        if auto_answers:
            selected_option = q["options"][auto_answers[idx - 1] - 1]
            print(f"Selected (auto): {selected_option}")
        else:
            while True:
                try:
                    answer = int(input("Enter the number of your answer: "))
                    if 1 <= answer <= len(q["options"]):
                        selected_option = q["options"][answer - 1]
                        break
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Please enter a number.")

        # Calculate points based on the answer
        points = q["points"][q["options"].index(selected_option)]
        total_points += points
#        print(f"Points for this question: {points}\n")
        print("\n")

    # Calculate the total percentage
    score_percentage = (total_points / max_points) * 100

    print("---\n\nResult:\n")
    print(f"Score: {score_percentage:.1f}%")

    if score_percentage >= 70:
        print("Category: Evolved Outlier")
        print("""
You embody a mindset of independent thought, personal authenticity, and deep internal integrity.
Rather than seeking validation from mass trends or popular opinion, you prioritize truth, principled conviction, and a profound understanding of yourself and the world around you.

Your loyalty is to reality — not to collective illusions, social pressures, or superficial acceptance.
You are willing to stand alone if necessary, choosing the discomfort of intellectual honesty over the ease of conformity.
Your commitment to authenticity often puts you at odds with mainstream culture, but it also enables you to experience deeper growth, more genuine relationships, and a life driven by personal meaning rather than external expectations.

While the path of the evolved outlier can be isolating at times, it grants a rare kind of freedom — the freedom to live by earned knowledge, uncompromised values, and an unshakable sense of self.
Your journey is not about fitting in; it is about standing firm, seeing clearly, and building a life that is truly your own.
        """)
    else:
        print("Category: Normie")
        print("""
You tend to align closely with the prevailing values, beliefs, and behaviors of the society around you.
Fitting in and maintaining social harmony are likely important priorities in your life, and you may naturally defer to established customs, traditions, or mainstream opinions rather than challenging or questioning them.

You might find comfort in shared experiences, community norms, and widely accepted viewpoints, preferring not to risk social friction by diverging from the majority.
Authenticity and independent thought may still matter to you on some level, but they are often subordinated to the need for belonging, acceptance, or avoiding conflict.

Critical self-examination and independent value formation may not be central focuses in your personal development. Instead, you may draw your sense of right, wrong, success, and meaning more from the expectations and validations of the group than from internally derived standards.

This orientation can provide stability, predictability, and a strong sense of community.
        """)

#run_quiz([1,1,2,1,1,2,1,2,5,2]) # 0%
#run_quiz([1,2,2,1,2,2,1,2,4,2]) # 7.5%
#run_quiz([2,4,1,2,4,1,2,1,2,1]) # 92.5%
#run_quiz([2,5,1,2,5,1,2,1,1,1]) # 100%

run_quiz()
