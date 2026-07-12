# import os
# from openai import OpenAI

# Read API key from environment variable
# api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. Please set it as an environment variable."
    )

client = OpenAI(api_key=api_key)

messages = []


def completion(user_message):
    global messages

    # Add user's message
    messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    assistant_reply = response.choices[0].message.content

    # Save assistant's response
    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply,
        }
    )

    print(f"Jarvis: {assistant_reply}")


if __name__ == "__main__":
    print("Jarvis: Hi! I am Jarvis. How may I help you?\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() in ["exit", "quit", "bye"]:
            print("Jarvis: Goodbye!")
            break

        completion(user_question)