responses = {
    "hello": "Hi there 👋",
    "how are you": "I'm functioning perfectly!",
    "your name": "I am a rule-based AI chatbot.",
    "what is ai": "AI means Artificial Intelligence.",
    "bye": "Goodbye 👋"
}

print("🤖 Rule-Based AI Chatbot Started")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("🤖", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that yet."
    )

    print("🤖", reply)