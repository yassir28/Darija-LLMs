from openai import OpenAI
client = OpenAI()
import pandas as pd
# dataframe and load of verbs
df = pd.read_csv('verbs.csv')
darija_verbs = df['n1'].tolist()
verbs_eng_translations = df['eng'].tolist() 
verbs_eng_translations = [verb.replace(" ", "_") for verb in verbs_eng_translations]


test = client.chat.completions.create(
model =  "gpt-3.5-turbo",
messages = [
    {
        "role": "system",
        "content": "You will be provided with a verb in Moroccan Darija language. Your task is to translate it into English and provide only its lemma as an output." + 
                    "The lemma of the translated verb should not contain 'to'."
    },
    {
        "role": "user", 
        "content": 'شم'
    }
],
temperature=0.1, # deterministic
#max_tokens=1, # in case of a dot
#top_p=0.1
# temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both.
# top_p:An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
# max_tokens: The maximum number of tokens that can be generated in the chat completion.

)

test = test.choices[0].message.content
print(test)