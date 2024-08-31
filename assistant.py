from openai import OpenAI

OPENAI_API_KEY = "INSERT-KEY-HERE"

client = OpenAI(api_key=OPENAI_API_KEY)

messages=[
  {"role": "system", "content": "You are a helpful assistant."},
]

while True:
  user_input = input("Mr. P: ")
  messages.append({"role": "user", "content": user_input})


  response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
  )

  res = response.choices[0].message.content
  messages.append({"role": "assistant", "content": res})

  print(res)
