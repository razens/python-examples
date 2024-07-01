import google.generativeai as genai

from google.colab import userdata

GOOGLE_API_KEY = userdata.get('AIzaSyCXNCWDlR3VykPR6CpHhUzVB6dRpOwJP-Q')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Give me python code to sort a list")
print(response.text)
