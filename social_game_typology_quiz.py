import shutil


def paginate_output(text: str):
    # Get terminal height
    try:
        terminal_height = shutil.get_terminal_size().lines
    except:
        terminal_height = 24  # fallback if terminal size can't be determined

    # Reserve a few lines for the prompt
    lines_per_page = terminal_height - 7

    lines = text.strip().split('\n')
    total_lines = len(lines)

    for i in range(0, total_lines, lines_per_page):
        page = lines[i:i + lines_per_page]
        print('\n'.join(page))
        if i + lines_per_page < total_lines:
            input("\n--- Press Enter to continue ---\n")


def run_quiz(auto_answers=None):
    questions = [
        # Self-Presentation
        {
            "question": "How often do you present a carefully crafted version of yourself rather than expressing how you feel in the moment?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you speak freely without worrying how others will perceive you?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you prefer authenticity over polish when sharing your thoughts?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you shape your behavior to meet social expectations rather than your internal sense of self?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you filter your expressions rather than letting them emerge spontaneously?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },

        # Emotional Exchange
        {
            "question": "How often do you try to create harmony in emotional interactions rather than share raw emotional states?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you value emotional transparency more than emotional comfort?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you reveal your emotional state even if it disrupts the mood?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you focus more on aligning emotionally with others than on being emotionally honest?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you prefer to regulate emotions to maintain peace rather than expressing them openly?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },

        # Cognitive Orientation
        {
            "question": "How often do you prefer abstract logic and structured models over intuitive insight?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you find comfort in loosely defined meanings rather than precise conceptual clarity?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you think in structured systems rather than metaphor and narrative?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you analyze meanings logically rather than intuitively feeling them out?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you rely more on definitional precision than on interpretive flexibility?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },

        # Dialogue Strategy
        {
            "question": "How often do you engage others in open-ended inquiry rather than trying to convince them of your view?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you frame your conversations to lead others toward your conclusions rather than co-discovering truth?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you use rhetorical strategy rather than mutual exploration in dialogue?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you prefer dialogue that leads to shared discovery over dialogue that persuades?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you aim for mutual understanding rather than winning an argument?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },

        # Communication Explicitness
        {
            "question": "How often do you prefer to state things explicitly rather than relying on implied context?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you expect others to 'read between the lines' rather than spelling things out?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you favor direct, literal communication over subtle or symbolic language?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you communicate in a way that assumes shared understanding rather than clear exposition?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you choose precision over suggestion when speaking?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },

        # Group Orientation
        {
            "question": "How often do you prioritize group harmony over personal convictions?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you navigate life based on inner principles more than belonging needs?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you value inclusion more than authenticity?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you stay true to your own course rather than adjusting to fit in?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you change your tone or behavior to be more acceptable to a group?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },

        # Relational Focus
        {
            "question": "How often do you connect based on aligned goals and values rather than emotional closeness?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you form relationships around shared emotional support rather than purpose?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you value shared ideals over emotional rapport in relationships?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        },
        {
            "question": "How often do you rely on deep feelings rather than shared convictions to bond with others?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Almost Never", "Rarely"],
            "points": [4, 3, 2, 1, 0]
        },
        {
            "question": "How often do you prioritize shared purpose more than emotional resonance?",
            "options": ["Almost Never", "Rarely", "Sometimes", "Often", "Almost Always"],
            "outlier_answers": ["Often", "Almost Always"],
            "points": [0, 1, 2, 3, 4]
        }
    ]


    print("Welcome to the Social Game Typology Test, version two!\n")

    total_points = 0
    max_points = 0

    for idx, q in enumerate(questions, 1):
        print(q["question"],"\n")
        for i, option in enumerate(q["options"], 1):
            print(f"  {i}. {option}")

        if auto_answers:
            selected_option = q["options"][auto_answers[idx - 1] - 1]
            print(f"Selected (auto): {selected_option}")
        else:
            while True:
                try:
                    answer = int(input("\nEnter the number of your answer: "))
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
        #print(f"Points for this question: {points}\n")
        print("\n")

    # Calculate the total percentage
    score_percentage = (total_points / max_points) * 100

    print("---\n\nResult:\n")
    #print(f"Total points: {total_points}")
    #print(f"  Max points: {max_points}")
    #print(f"       Score: {score_percentage:.1f}%")

    if score_percentage >= 96:
        print("    Category: 🏛️  Transcendent Architect\n")
        paginate_output("""
Description:  

This is the rare individual who has fully internalized their own system of 
meaning, functioning independently of societal scripts. They do not resist 
the norm — they transcend it. Their orientation to life is radically 
self-authored, deeply integrated, and often solitary.

Figures:

- Siddhartha Gautama (Buddha) – Left the societal roles of royalty and 
  identity entirely to pursue and embody a wholly self-authored system of 
  truth.
- Diogenes of Sinope – Lived in radical autonomy, rejecting social conventions
  to the point of public ridicule or awe.
- Ayn Rand – A radical philosopher who challenged the moral foundations of
  society, advocating a self-authoring, rational egoism that defied both 
  emotional and cultural norms.

Traits:

- Expresses self with complete autonomy and emotional sovereignty
- Views culture as one lens among many — not a defining force
- Often uninterested in conventional success or recognition
- Embodies integrity, clarity, and depth across all dimensions
- Creates presence, frameworks, or art that alter others' perception

Social Role:  

A living anomaly. These individuals often exist outside of 
classification. They may be sages, innovators, or existential 
outsiders — those who walk alone, not by rejection, but by design.
        """)
    elif score_percentage >= 91:
        print("    Category: 🛤️  Ideological Trailblazer\n")
        paginate_output("""
Description:  

Ideological Trailblazers inhabit the boundary between worlds — between 
accepted norms and emerging paradigms. They operate with little 
need for social affirmation, and often carry a heightened 
sensitivity to truth, falsehood, and existential integrity.

Figures:

- David Bowie – Constantly reinvented his identity, blending 
  gender, art, philosophy, and performance outside the boundaries 
  of normativity.
- Terence McKenna – Explored and promoted visionary states, 
  cultural critique, and deep-time thinking that disrupted scientific 
  and spiritual orthodoxy.
- Baruch Spinoza – Lived independently of religious dogma, 
  developing a philosophy of existence that would only later be 
  recognized as profound.


Traits:

- Moves fluidly between multiple social and philosophical frameworks
- Lives comfortably in ambiguity, contradiction, or liminal states
- Rejects simplistic binaries and ideological dogma
- Prioritizes inner alignment over external approval
- May appear aloof, mystical, or iconoclastic to others

Social Role:  

A translator between paradigms. Ideological Trailblazers are often 
misunderstood but can serve as powerful guides for others crossing 
thresholds of awareness or identity.
        """)
    elif score_percentage >= 86:
        print("    Category: 🔭 Visionary\n")
        paginate_output("""
Description:  

The Visionary exhibits behaviors and ideas that prefigure future 
social norms. Their thinking often challenges foundational 
assumptions of the culture they inhabit. They may not always be 
understood, but they operate with a sense of inner necessity and 
clarity.

Figures:

- Nikola Tesla – Imagined technologies and paradigms well ahead of
  his time, largely misunderstood in his era.
- Elon Musk – A norm-defying innovator who bends industries and public 
  discourse to his will, often at the cost of conventional behavior or 
  emotional attunement.
- Jiddu Krishnamurti – Rejected organized religion and traditional 
  structures of authority in favor of direct personal insight.

Traits:

- Holds and communicates insights ahead of mainstream comprehension
- May feel alienated but self-assured
- Strong focus on meaning, truth, and personal evolution
- Unwilling to compromise core convictions for social approval
- Viewed by others as intense, original, or unconventional

Social Role:  

A cultural prototype. Visionaries rarely fit cleanly into existing 
categories and often act as seers, creatives, or radical reformers.
They influence indirectly by modeling a way of being that others 
can feel, even if they can't yet name.
          """)
    elif score_percentage >= 81:
        print("    Category: 🧠 Synthesizer\n")
        paginate_output("""
Description:  

The Synthesizer bridges internal depth with external expression. They 
have developed a personal system of meaning that integrates values 
such as autonomy, emotional depth, and intellectual clarity. Rather 
than merely resisting norms, they restructure them.

Figures:

- Carl Jung – Synthesized mysticism, science, and psychology into a 
  new model of the human psyche.
- Rachel Carson – Brought ecology, science, and emotional urgency 
  together in Silent Spring, changing environmental discourse.
- Alan Watts – Translated Eastern philosophy into terms digestible 
  to the West, forming bridges between differing cultural frameworks.

Traits:

- Creates frameworks for understanding not yet widely accepted
- Communicates with philosophical or psychological depth
- Actively redefines connection, belonging, and dialogue
- Expresses coherence between inner world and outer actions
- Often builds new ways to relate without rejecting others

Social Role:  

A builder of alternative culture. Synthesizers form their own 
micro-tribes, ideologies, or practices and model new forms of 
living that others may later adopt.
          """)
    elif score_percentage >= 76:
        print("    Category: 🧭 Divergent\n")
        paginate_output("""
Description:  

This range reflects someone who often deviates from social norms, 
not out of rebellion, but from a deeper commitment to inner values 
and authenticity. They experience tension with the expectations of 
mainstream culture and frequently prioritize clarity, honesty, 
and autonomy over conformity.

Figures:

- Franz Kafka – His deeply introspective, often alienated literary 
  voice explored the absurdity of modern life, well outside 
  mainstream sensibilities.
- James Baldwin – Honest and personal in his critique of race, 
  identity, and society, standing apart from both mainstream and 
  radical ideologies of his time.
- Simone Weil – A mystic-philosopher and social critic who fused 
  rigorous ethical introspection with a radical rejection of power 
  and privilege, often misunderstood even by her contemporaries.

Traits:

- Frequently prioritizes authentic expression over likability
- Shows discomfort with performative social norms
- Displays emerging independence of thought
- Values truthfulness, even when socially inconvenient
- May struggle with feeling “out of sync” but still seeks some 
  connection

Social Role:  

A quiet challenger of the norm. These individuals begin to stand 
apart in visible ways and may initiate small ripples of change in 
their communities. They are still partially engaged with the 
mainstream, but no longer dependent on its validation.
          """)
    else:
        print("    Category: 👥 Normal (or \"Normie\")\n")
        paginate_output("""
Description:  

A normal person aligns with mainstream expectations in both 
behavior and thought. They typically balance social conformity with 
some degree of individuality, but rarely to a disruptive extent. 
Their responses indicate a tendency to adapt to social cues, 
uphold conventional standards, and prioritize group cohesion over 
radical self-expression or ideological divergence.

Traits:

- Conforms to accepted social roles and behaviors
- Communicates in expected, socially safe ways
- Seeks moderate intimacy, authenticity, and autonomy, but within 
  culturally reinforced boundaries
- Values harmony and avoids polarizing or controversial stances
- Exhibits a stable, relatable identity that rarely challenges the 
  group

Social Role:  

They are the cultural anchor points — representative of the 
majority. This person tends to maintain the continuity of existing 
norms and is often perceived as reliable, stable, and cooperative. 
They are not agents of change, but neither are they hostile to it; 
they might follow innovation once it’s widely adopted, but rarely 
initiate it.
        """)


#
# Sample, automated quiz mode. Uncomment only one "run_quiz" line at a time.
#
#run_quiz([5,1,1,5,5,5,1,1,5,5,1,5,1,1,1,1,5,5,1,1,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1])  #   0.0% (Normie)
#run_quiz([5,1,1,5,5,5,1,1,1,1,5,1,5,5,5,5,1,1,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5])  #  77.1% (Divergent)
#run_quiz([5,1,1,5,5,5,5,5,1,1,5,1,5,5,5,5,1,1,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5])  #  82.9% (Synthesizer)
#run_quiz([5,1,1,5,1,1,5,5,1,1,5,1,5,5,5,5,1,1,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5])  #  88.6% (Visionary)
#run_quiz([5,1,5,1,1,1,5,5,1,1,5,1,5,5,5,5,1,1,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5])  #  94.3% (Ideological Trailblazer)
#run_quiz([1,5,5,1,1,1,5,5,1,1,5,1,5,5,5,5,1,1,5,5,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5])  # 100.0% (Transcendent Architect)

#
# Interactive mode. Uncomment this "run_quiz" line out to run in interactive, non-automated mode.
#
run_quiz()
