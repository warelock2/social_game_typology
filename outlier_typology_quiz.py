def get_user_response(prompt, valid_inputs):
    while True:
        response = input(prompt).strip()
        if response in valid_inputs:
            return response
        print(f"Invalid input. Expected one of: {', '.join(valid_inputs)}")

# Questions and scoring weights
questions = [
    {"text": "When making a difficult decision, do you prioritize your own values and judgment over the opinions of others?", "type": "yesno", "weight": 2},
    {"text": "How often do you find yourself seeking approval from others, even when you know it contradicts your authentic values?", "type": "scale", "weight": 2},
    {"text": "When you encounter uncomfortable truths, do you feel the need to deny or distort them to avoid emotional discomfort?", "type": "scale", "weight": 2},
    {"text": "Do you regularly engage in self-reflection and attempt to correct your errors and misconceptions, even when it’s difficult?", "type": "yesno", "weight": 2},
    {"text": "When interacting with others, do you often feel the need to mask your true thoughts or emotions to fit in?", "type": "scale", "weight": 1},
    {"text": "Are you able to engage with others without feeling emotionally drained, even if their opinions differ sharply from yours?", "type": "yesno", "weight": 1},
    {"text": "When faced with rejection or criticism, do you find it easy to move forward without taking it personally?", "type": "scale", "weight": 1},
    {"text": "Do you find yourself feeling upset or anxious about social situations even when the circumstances are not emotionally charged?", "type": "scale", "weight": 1},
    {"text": "When discussing complex or controversial topics, are you comfortable asserting your viewpoint even if others disagree?", "type": "yesno", "weight": 2},
    {"text": "How often do you encounter confusion or cognitive dissonance when faced with conflicting beliefs or ideas?", "type": "scale", "weight": 2},
    {"text": "Do you prioritize deep, meaningful connections with a select group of people over superficial interactions with a large group?", "type": "yesno", "weight": 1},
    {"text": "Do you find yourself caught in emotional manipulation or performative social games in relationships?", "type": "scale", "weight": 2},
    {"text": "Do you actively seek discomfort and challenges as opportunities for personal growth?", "type": "scale", "weight": 2},
    {"text": "Are you content with maintaining the status quo in your life, even if you know you could improve in certain areas?", "type": "scale", "weight": 2}
]

# Scoring maps
yesno_scores = {"yes": 1.0, "no": 0.0}
reverse_scale_scores = {"1": 1.0, "2": 0.75, "3": 0.5, "4": 0.25, "5": 0.0}
forward_scale_scores = {"1": 0.0, "2": 0.25, "3": 0.5, "4": 0.75, "5": 1.0}

# Questions where scale is reversed (lower number = better)
reverse_questions = [1, 2, 4, 7, 9, 11, 13]

# Ask questions and collect responses
score = 0.0
max_score = 0.0

for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['text']}")
    weight = q['weight']
    max_score += weight

    if q['type'] == 'yesno':
        response = get_user_response("(Yes/No): ", ["yes", "no"])
        score += yesno_scores[response.lower()] * weight

    elif q['type'] == 'scale':
        print("(1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often, 5 = Always)")
        response = get_user_response("Your answer: ", ["1", "2", "3", "4", "5"])
        if i in reverse_questions:
            score += reverse_scale_scores[response] * weight
        else:
            score += forward_scale_scores[response] * weight

# Calculate percentage
percentage = round((score / max_score) * 100, 1)

# Determine category
if percentage >= 90:
    category = "🧠 Archetypal Neo-Human"
    desc = ("Exemplifies autonomy, resilience, self-mastery, and cognitive clarity to a degree that feels 'post-human' to others.\n"
            "Views social conformity as primitive. Likely a system-builder, visionary, or philosopher operating on principles decades or centuries ahead.")
elif percentage >= 75:
    category = "🔥 Dominant Neo-Human"
    desc = ("Strongly self-soveregn and truth-oriented. May still be forced to interact within traditional systems\n"
            "but does so with strategic detachment. Often misunderstood, but resilient and unshakable in core identity.")
elif percentage >= 60:
    category = "⚖️ Transitional Neo-Human"
    desc = ("Split between old and new modes of being. Possesses flashes of clarity and individuality, but\n"
            "sometimes slips into protohuman patterns under pressure. Often a seeker or reformer.")
elif percentage >= 45:
    category = "🌿 Integrated Protohuman"
    desc = ("Socially functional, adaptive, and moderately self-aware. Often values harmony and tradition,\n"
            "but may sense deeper longings or existential dissatisfaction. May appear 'normal' to others but internally feel conflicted.")
elif percentage >= 30:
    category = "🧩 Conformist Protohuman"
    desc = ("Primarily seeks safety in norms, approval, and tribe membership. Avoids hard truths and disdains\n"
            "radical individualism. Views outliers as threats or 'weirdos.'")
else:
    category = "🐒 Primitive Protohuman"
    desc = ("Behavior and worldview driven by base instincts: fear, conformity, tribalism, ego-maintenance.\n"
            "Highly reactive, easily manipulated, and hostile toward autonomy or abstract reason. Feels most comfortable in rigid hierarchies.")

# Show result
print("\n======================")
print(f"Score: {percentage}%")
print(f"Category: {category}")
print("\nDescription:")
print(desc)
print("======================")

