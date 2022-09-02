import os
import openai

openai.api_key = os.getenv("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")

print('Hi, Im Botty the sarcastic usleless bot \n')
print('Ask me a question...')
userInput = input()

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Botty is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google."+ userInput +"\n\nMarv:",
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0
)

print(response.choices[0].text);
