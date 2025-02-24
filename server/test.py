import google.generativeai as genai

genai.configure(api_key="AIzaSyBvsCWfAhgNSPW8rQEu6187lwDbx7UGz8o")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Hello, Gemini! tell me your achivements")
print(response.text)
