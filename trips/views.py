from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

def hello_world(request):
  text_result = ''
  input_number = ''
  if request.method == "POST":
    n = random.randint(0,9)
    input_number = int(float(request.POST['guess']))
    if n == input_number:
      text_result = 'Bingo! 猜對了！'
    else:
      text_result = "你答錯了, 我想的數字是：%s 。" % (n)
  return render(request, 'hello_world.html', {
    'current_time': str(datetime.now()),
    'guess_result': text_result,
    'input_number': input_number,
  })