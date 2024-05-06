from django.shortcuts import render
import requests
import markdown
import google.generativeai as genai

#keep it secret, I'll delete mine after this project
GEMINI_API_KEY = 'AIzaSyAHJf66uQqUKcIjSHiLC4aXQVHQvGKCDsI'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Create your views here.
def index(request):
    response_text = None
    processed_text = None
    context = {}

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        if user_input:
            response = model.generate_content(user_input)
            response_text = response.text
            processed_text = markdown.markdown(response_text)

        else:
            response_text = "Please enter your question."

        context = {
            'processed_text': processed_text,
            'user_input': user_input,
        }
    return render(request, 'index.html', context=context)