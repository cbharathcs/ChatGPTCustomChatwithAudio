import openai
openai.api_key = "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"

def ask_question(question, model="text-davinci-002"):
    response = openai.Completion.create(
      engine=model,
      prompt=question,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer
answer = ask_question("What is the capital of France?")
print(answer)