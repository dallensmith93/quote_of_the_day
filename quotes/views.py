from django.shortcuts import render
from .models import Quote
import random

def quote_of_the_day(request):
    quotes = Quote.objects.all()
    
    if quotes.exists():
        quote = random.choice(quotes)
    else:
        
        quote = Quote(text="the world", author="Admin")
    
    return render(request, 'quotes/quote_of_the_day.html', {'quote': quote})