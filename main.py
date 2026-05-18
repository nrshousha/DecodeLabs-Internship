responses= {
    "hello": "Hi there, How can I help you?",
    "bye": "Bye bye",
    "what is Artificial Intelligence?": "Artificial Intelligence (AI) is the simulation of human intelligence in machines that can learn, reason, and make decisions.",
    "what is Machine Learning?": "Machine Learning is a branch of AI that allows computers to learn patterns from data without being explicitly programmed.",
    "what is Python used for in AI?": "Python is widely used in AI because it is simple, powerful, and has many libraries for machine learning and data analysis.",
    "what is a chatbot?": "A chatbot is a program designed to simulate conversation with users through text or voice interactions.",
    "what is Deep Learning?": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to process complex data.",
    "what are neural networks?": "Neural networks are computer systems inspired by the human brain that help machines recognize patterns and solve problems.",
    "why is AI important?": "AI helps automate tasks, improve decision-making, and create smart systems used in healthcare, business, education, and more."
}

user_input = input("Bot: I'm Your AI assistant.\nYou: ").lower().strip()

while True:
    reply = responses.get(user_input, "I don't know what you are looking for.")
    user_input = input(f"Bot: {reply}\nYou: ")
    if user_input == "bye":
        print(f'Bot: {responses["bye"]}')
        break
