from django.shortcuts import render
from .models import *
from .forms import *

def show_main_page(request):
    return render(request, 'finder/main_page.html')



def show_big_text_page(request):
    if request.method == 'POST':
        form = AddTextFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddTextFileForm()
    return render(request, 'finder/add_file.html', {'form': form})

def show_big_text_searching(request, unique_title, unique_number):
    search_query = request.GET.get('search', '')
    if search_query:
        file = AddTextFile.objects.get(unique_title=unique_title, unique_number=unique_number)
        text = file.file
        str = ''
        with open(f'media/{text}', 'r', encoding='utf-8') as f:
            for line in f:
                if search_query in line:
                    str += line
                    str += '<br>'
    else:
        file = AddTextFile.objects.get(unique_title=unique_title, unique_number=unique_number)
        text = file.file
        str = ''
        with open(f'media/{text}', 'r', encoding="utf-8") as f:
            for line in f:
                str += f'{line}'
                str += '<br>'
    return render(request, 'finder/show_text_searching.html', {'str':str, 'unique_title': unique_title, 'unique_number':unique_number})



