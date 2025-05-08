from flask import Flask, render_template_string, render_template, request

app = Flask(__name__)

# Global list of quiz questions
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
    },
]

total_questions = len(questions)
max_points = sum(max(q['points']) for q in questions)

@app.route('/')
def index():
    return render_template_string("""
    <html>
        <head><title>Home</title></head>
        <body>
            <h1>Welcome to the Social Game Typology Quiz!</h1>
            By warelock<p>
            This was inspired by <a href="https://noise.afobl.com/the-untethered-path-of-the-self-sovereign-individual/">The Untethered Path of the Self-Sovereign Individual</a>.<p>
            <hr>
            <p>
            <li>
              <a href="/quiz">Start the Social Game Typology Quiz</a>
            </li>
            <p>
            <hr>
            Here is the <a href="https://github.com/warelock2/social_game_typology">source code</a> to this quiz.<p>
        </body>
    </html>
    """)

@app.route('/quiz', methods=['GET'])
def quiz():
    return render_template_string("""
    <html>
        <head><title>Quiz</title></head>
        <body>
            <h1>The Social Game Typology Quiz</h1>
            There are a total of {{ total_questions }} questions on this quiz.<p>
            <p>
            NOTICE: A.I. tools were used during the creative process of this psychological quiz.<p>
            <p>
            <hr>
            <p>
            <form method="post" action="/results">
                {% for q in questions %}
                    {% set idx = loop.index0 %}
                    <p>{{ q.question }}</p>
                    {% for i in range(5) %}
                        <input type="radio" name="q{{ idx }}" value="{{ i+1 }}" required>
                        {{ i+1 }} - {{ q.options[i] }}<br>
                    {% endfor %}
                    <br>
                {% endfor %}
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """, questions=questions, total_questions=total_questions)

@app.route('/results', methods=['POST'])
def results():
    responses = []
    for idx in range(len(questions)):
        answer = request.form.get(f'q{idx}')
        responses.append(int(answer) if answer else None)
    total_points = sum(questions[i]['points'][response - 1] for i, response in enumerate(responses))
    score_percentage = (total_points / max_points) * 100

    if score_percentage >= 95:
        response_content = "response_transcendental_architect.html"
    elif score_percentage >= 91:
        response_content = "response_ideological_trailblazer.html"
    elif score_percentage >= 86:
        response_content = "response_visionary.html"
    elif score_percentage >= 81:
        response_content = "response_synthesizer.html"
    elif score_percentage >= 76:
        response_content = "response_divergent.html"
    else:
        response_content = "response_normie.html"

    preamble_content = render_template_string("""
        <h1>Thank you for taking the Social Game Typology Quiz!</h1><p>
        <p>
        Your responses: {{ responses }}<p>
        <p>
        Your results:<p>
        <p>
        <hr>
        <p>
        """, responses=responses, total_points=total_points, max_points=max_points, score_percentage=score_percentage)

    full_content = preamble_content + "<pre>" + render_template(response_content) + "</pre>"

    return full_content

if __name__ == '__main__':
    app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'), port=8443)

