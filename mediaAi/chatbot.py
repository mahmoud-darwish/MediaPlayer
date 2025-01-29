import google.generativeai as genai


def chat(text):
        
    GOOGLE_API_KEY='AIzaSyDdjI5zrjt3bawltH1v0dRdOnvC6RGvWOM'

    genai.configure(api_key=GOOGLE_API_KEY)


    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)

    return response.text

# print(response.text)