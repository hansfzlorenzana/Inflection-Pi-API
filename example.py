from pi import Pi

prompt = "How are you?"

chatbot = Pi("TOKEN HERE", proxy=False)

response = chatbot.send_message(prompt)

print(response)
