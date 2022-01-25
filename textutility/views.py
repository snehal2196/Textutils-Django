# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
from datetime import datetime
from textutility.models import Contact
from django.contrib import messages
 


def home(request):
    return render(request, 'index.html')
    

def analyze(request):
    djtext = request.GET.get('text', 'default')
  
    name = request.GET.get('analyzeRadio')
    lang = request.GET.get('lang')
    
    if name == 'removepunc':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char 
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif name == 'uppercase':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif name == 'capfirst':
        analyzed = djtext.title()
        params = {'purpose': 'Capitalize first letter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        
    elif name == 'removespace':
        analyzed = ''
        for index,char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed = analyzed + char
                
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)   

    elif name == 'charcount':
        analyzed = ''
        count = 0
        for char in djtext:
            if char == ' ':
                continue
            else:
                count+=1 

        analyzed = f"Total character counts are {count}"       
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)   

    elif lang == 'hindi':
        translator = Translator()
        translation = translator.translate(djtext, dest='hi')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params) 

    elif lang == 'gujarati':
        translator = Translator()
        translation = translator.translate(djtext, dest='gu')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)  

    elif lang == 'marathi':
        translator = Translator()
        translation = translator.translate(djtext, dest='mr')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)   

    elif lang == 'english':
        translator = Translator()
        translation = translator.translate(djtext, dest='en')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'punjabi':
        translator = Translator()
        translation = translator.translate(djtext, dest='pa')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'sindhi':
        translator = Translator()
        translation = translator.translate(djtext, dest='sd')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'kannada':
        translator = Translator()
        translation = translator.translate(djtext, dest='kn')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'bengali':
        translator = Translator()
        translation = translator.translate(djtext, dest='bn')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'tamil':
        translator = Translator()
        translation = translator.translate(djtext, dest='ta')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    elif lang == 'telugu':
        translator = Translator()
        translation = translator.translate(djtext, dest='te')
        text = translation.text
        params = {'purpose': 'Translated to Hindi', 'analyzed_text': text}
        return render(request, 'analyze.html', params)

    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact.save()
        messages.success(request, 'Your message has been submitted!')

    return render(request, 'contact.html')

# def analyze(request):
#     djtext = request.GET.get('text', 'default')
#     removepunc = request.GET.get('removepunc', 'off')
#     uppercase = request.GET.get('uppercase','off')
#     capfirst = request.GET.get('capfirst', 'off')
#     removespace = request.GET.get('removespace', 'off')
#     charcount = request.GET.get('charcount' , 'off')

#     if removepunc == 'on':
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ''
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed += char
#         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)

    

#     elif uppercase == 'on':
#         analyzed = ''
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params = {'purpose': 'Convert to uppercase', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)

#     elif capfirst == 'on':
#         analyzed = djtext.title()
#         params = {'purpose': 'Capitalize first letter', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)
        
#     elif removespace == 'on':
#         analyzed = ''
#         for index,char in enumerate(djtext):
#             if djtext[index] == ' ' and djtext[index+1] == ' ':
#                 pass
#             else:
#                 analyzed = analyzed + char
                
#         params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)   

#     elif charcount == 'on':
#         analyzed = ''
#         count = 0
#         for char in djtext:
#             if char == ' ':
#                 continue
#             else:
#                 count+=1 

#         analyzed = f"Total character counts are {count}"       
#         params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
#         return render(request, 'analyze.html', params)          

#     else:
#         return HttpResponse('Uhhh, please select atleast one option!')

