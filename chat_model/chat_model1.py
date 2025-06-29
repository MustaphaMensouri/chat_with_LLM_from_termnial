from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


load_dotenv()
model_names = ['gpt-4','claude 3.5 sonnet','gemini 2.0 flash']
model_name = "gemini-2.0‑flash"
while True:
    print("Which model would you like to talk to?")
    for i in range(len(model_names)):
        print(f"- {i+1}  {model_names[i]}") 
    model_name = input("Enter its name:")
    if model_name in model_names:
        break
    else:
        print("please try again")

if model_name == 'gpt-4' or model_name == '1':
    model = init_chat_model("gpt-4", model_provider="openai")
    
elif model_name == 'claude 3.5 sonnet' or model_name == '2':
    model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

else:
    model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


print("-"*50)
print(f"You are currently chatting with {model_name}")
print("-"*50)

while True:
    userinput = input("you: ")
    if userinput == "exit":
        break

    result = model.invoke(userinput)

    print(f'{model_name}: {result.content}')
