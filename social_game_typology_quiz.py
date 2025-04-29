def run_quiz(auto_answers=None):
    questions = [
        {
            "question": "When making a difficult decision, do you prioritize your own values and judgment over the opinions of others?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [8, 0]
        },
        {
            "question": "How often do you find yourself seeking approval from others, even when you know it contradicts your authentic values?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [8, 6, 4, 2, 0]
        },
        {
            "question": "When you encounter uncomfortable truths, how often do you consciously avoid denying or distorting them, while embracing seemingly necessary emotional discomfort?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 2, 4, 6, 8]
        },
        {
            "question": "Do you regularly engage in self-reflection and attempt to correct your errors and misconceptions, even when it’s difficult?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [8, 0]
        },
        {
            "question": "When interacting with others, how often do you feel comfortable masking your true thoughts or emotions, if it appears that by doing so, you might have a better chance to fit in?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "Have you ever felt the courage to attempt to rationally engage with others, even if their opinions differ sharply from yours?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]
        },
        {
            "question": "When faced with justified rejection or constructive criticism, how often do you find it easy to move forward without taking it personally?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "When discussing complex or controversial topics, are you uncomfortable asserting your viewpoint if others might disagree?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 8]
        },
        {
            "question": "How often do you encounter confusion or cognitive dissonance when faced with conflicting beliefs or ideas?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [8, 6, 4, 2, 0]
        },
        {
            "question": "Do you prioritize casual interactions with a large group over deep, meaningful connections with a select group of people?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]
        },
        {
            "question": "How often do you find yourself caught up in and/or instigating emotional manipulation or performative social games in relationships?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [8, 6, 4, 2, 0]
        },
        {
            "question": "How often do you actively seek discomfort and challenges as opportunities for personal growth?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 2, 4, 6, 8]
        },
        {
            "question": "How often are you content with maintaining the intellectual status quo in your life, even if you know you could improve in certain areas?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [8, 6, 4, 2, 0]
        },
        {
            "question": "When it comes to relationships, do you value social norms and appearances more than deep emotional connection and personal authenticity?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]
        },
        {
            "question": "How often do you feel that being manipulative or insincere is not justified and causes problems in the long run?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "When making decisions, do you prefer to rely on logic and factual understanding over following popular trends or emotional comfort?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]
        },
        {
            "question": "In social or professional situations, do you prioritize agreeing with others for the sake of harmony over meaningful dialogue and intellectual honesty?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]
        },
        {
            "question": "How often are you frustrated that people avoid being direct or honest, instead relying on subtle signals or unspoken communication?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Often", "Almost always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "When faced with mainstream beliefs or societal expectations, do you tend to question and/or reject them if they conflict with your personal values?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]
        },
        {
            "question": "Do you believe it is more natural that romantic relationships are be based on external status and/or surface appearance rather than mutual respect, potentially harsh truths, and compatibility?",
            "options": ["Yes", "No"],
            "outlier_answers": ["No"],
            "points": [0, 4]
        },
        {
            "question": "When choosing your social circle, do you prioritize deep connections and shared values over fitting in with popular groups or trends?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]
        },
        {
            "question": "How often do you prefer things that most people find meaningful and entertaining, rather than feel disconnected or alienated by those things?",
            "options": ["Almost never", "Rarely", "Sometimes", "Often", "Almost always"],
            "outlier_answers": ["Almost never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "Do you value objective truth more than social approval or acceptance?",
            "options": ["Yes", "No"],
            "outlier_answers": ["Yes"],
            "points": [4, 0]
        }
    ]

    print("Welcome to the Social Game Typology Test!\n")

    total_points = 0
    max_points = 0

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
        max_points += max(q["points"])
#        print(f"Points for this question: {points}\n")
        print("\n")

    # Calculate the total percentage
    score_percentage = (total_points / max_points) * 100

    print("---\n\nResult:\n")
#    print(f"Total points: {total_points}")
#    print(f"  Max points: {max_points}")
#    print(f"       Score: {score_percentage:.1f}%")

    if score_percentage >= 90:
        print("    Category: 🧠 Archetypal Neo-Human")
        print("""
  o  Exemplifies autonomy, resilience, self-mastery, and cognitive clarity to a degree that feels "post-human" to others.
  o  Views social conformity as primitive.
  o  Likely a system-builder, visionary, or philosopher operating on principles decades or centuries ahead.
        """)
    elif score_percentage >= 75:
        print("    Category: 🔥 Dominant Neo-Human")
        print("""
  o  Strongly self-sovereign and truth-oriented.
  o  May still be forced to interact within traditional systems but does so with strategic detachment.
  o  Often misunderstood, but resilient and unshakable in core identity.
        """)
    elif score_percentage >= 70:
        print("    Category: ⚖️  Transitional Neo-Human")
        print("""
  o  Split between old and new modes of being.
  o  Possesses flashes of clarity and individuality, but sometimes slips into protohuman patterns under pressure or in social environments.
  o  Often a seeker or reformer.
        """)
    else:
        print("    Category: 👥 Normal (or \"Normie\")")
        print("""
You tend to align closely with the prevailing values, beliefs, and behaviors of the society around you.
Fitting in and maintaining social harmony are likely important priorities in your life, and you may naturally defer to established customs, traditions, or mainstream opinions rather than challenging or questioning them.

You might find comfort in shared experiences, community norms, and widely accepted viewpoints, preferring not to risk social friction by diverging from the majority.
Authenticity and independent thought may still matter to you on some level, but they are often subordinated to the need for belonging, acceptance, or avoiding conflict.

Critical self-examination and independent value formation may not be central focuses in your personal development. Instead, you may draw your sense of right, wrong, success, and meaning more from the expectations and validations of the group than from internally derived standards.

This orientation can provide stability, predictability, and a strong sense of community.
        """)

#
# Sample, automated quiz mode. Uncomment only one "run_quiz" line at a time.
#
#run_quiz([2,5,1,2,5,2,1,1,5,1,5,1,5,1,1,2,1,1,2,1,2,5,2]) #   0.0% (Normie)
#run_quiz([1,1,1,2,5,2,1,1,5,1,5,1,5,1,1,2,1,1,2,1,2,5,2]) #  12.5% (Normie)
#run_quiz([2,5,1,2,5,1,5,2,1,2,1,5,1,2,5,1,2,5,1,2,1,1,1]) #  71.9% (Transitional Neohuman)
#run_quiz([2,5,5,1,1,1,5,2,1,2,1,5,1,2,5,1,2,5,1,2,1,1,1]) #  87.5% (Dominant Neohuman)
#run_quiz([1,1,5,1,1,1,5,2,1,2,1,5,1,2,5,1,2,5,1,2,1,1,1]) # 100.0% (Archetypal Neohuman)

#
# Interactive mode. Uncomment this "run_quiz" line out to run in interactive, non-automated mode.
#
run_quiz()
