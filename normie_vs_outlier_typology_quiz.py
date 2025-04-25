questions = [
    {
        "text": "Q1: Do you feel that people's character and depth matter more than their physical appearance or social image?",
        "type": "yesno",
    },
    {
        "text": "Q2: How often do you feel frustrated by emotionally manipulative or performative behavior in social situations?",
        "type": "scale",
        "scale": {
            "1": "Never: I rarely notice or care about such behavior.",
            "2": "Rarely: Occasionally irritating, but I can overlook it.",
            "3": "Sometimes: It bothers me now and then.",
            "4": "Often: It’s a regular theme I observe and feel alienated by.",
            "5": "Always: This is a constant and conscious irritation for me."
        }
    },
    {
        "text": "Q3: Do you feel more comfortable facing hard truths than seeking emotional comfort in feel-good stories or groupthink?",
        "type": "yesno",
    },
    {
        "text": "Q4: In debates or conversations, do you prefer intellectually honest dialectic over persuasive rhetoric or social positioning?",
        "type": "yesno",
    },
    {
        "text": "Q5: How often do you feel social communication is filled with evasion, dishonesty, and hidden signals?",
        "type": "scale",
        "scale": {
            "1": "Never: People are usually direct and clear.",
            "2": "Rarely: I don’t often detect such subtext.",
            "3": "Sometimes: It’s there but not overwhelming.",
            "4": "Often: It bothers me how indirect people are.",
            "5": "Always: Communication often feels like a maze of unspoken games."
        }
    },
    {
        "text": "Q6: Do you often reject mainstream values or social pressure when they conflict with your personal standards?",
        "type": "yesno",
    },
    {
        "text": "Q7: Do you see romantic relationships as sacred partnerships rooted in truth and compatibility rather than theatrics or status?",
        "type": "yesno",
    },
    {
        "text": "Q8: When choosing your social circle, do you prioritize shared principles and mental clarity over popularity or trendiness?",
        "type": "yesno",
    },
    {
        "text": "Q9: How often do you feel alienated by what most people seem to find meaningful or entertaining?",
        "type": "scale",
        "scale": {
            "1": "Never: I generally enjoy and relate to popular interests.",
            "2": "Rarely: I diverge occasionally, but fit in most of the time.",
            "3": "Sometimes: I often feel a mild disconnect.",
            "4": "Often: I rarely relate to what most people value.",
            "5": "Always: I feel fundamentally at odds with the mainstream."
        }
    },
    {
        "text": "Q10: Are you more interested in what is *true* than in what is *acceptable*?",
        "type": "yesno",
    }
]

def ask_question(q):
    print(q["text"])
    if q["type"] == "yesno":
        while True:
            a = input("Answer (Yes/No): ").strip().lower()
            if a in ["yes", "no"]:
                return 1 if a == "yes" else 0
            print("Please enter 'Yes' or 'No'.")
    elif q["type"] == "scale":
        for k, v in q["scale"].items():
            print(f"{k}: {v}")
        while True:
            a = input("Answer (1-5): ").strip()
            if a in ["1", "2", "3", "4", "5"]:
                return 1 if int(a) >= 4 else 0
            print("Please enter a number from 1 to 5.")
    print()

def main():
    print("=== Normie vs. Outlier Test ===\n")
    print("Answer each question honestly to discover which category you are in.\n")

    score = 0
    for q in questions:
        print()
        score += ask_question(q)

    print("\n=== RESULT ===\n")
    if score >= 6:
        print("🧬 You are an Outlier.")
        print("""
Outliers live by inner truth rather than social approval. 
You likely prefer mental clarity, radical honesty, and meaningful connection 
over performance, emotional games, or surface-level validation.

You prioritize:

- Authenticity: Earned truth and substance rather than surface, manufactured image
- Emotional Integrity: True connection and honesty over manipulative flattery
- Lucidity: Understanding and intellectual integrity over sentimental comfort
- Discourse: Truth-seeking dialogue over rhetorical manipulation
- Candor: Clear signals and honesty over evasion and ambiguity
- Autonomy: Individual standards over herd belonging
- Intimacy: Sacred partnerships over romantic bait-and-switch
        """)
    else:
        print("🧢 You are a Normie.")
        print("""
Normies feel at home in the mainstream. You likely prioritize harmony, social approval, 
emotional ease, and conventional norms over challenging truths or abstract ideals. 
You may value fitting in, comfort, and mutual flattery more than deep candor or mental intensity.

You prioritize:

- Surface Appearance: Social image over earned depth
- Emotional Ease: Avoiding discomfort over truth
- Sentimental Familiarity: Comfort over intellectual rigor
- Rhetoric: Social harmony over rigorous debate
- Evasion: Ambiguity and "niceness" over directness
- Herd Approval: Belonging over individuality
- Romantic Theatrics: Feelings and excitement over compatibility and truth
        """)

if __name__ == "__main__":
    main()

