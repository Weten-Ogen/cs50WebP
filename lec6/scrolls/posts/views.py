from django.shortcuts import render
import time
from django.http import JsonResponse

# Create your views here.

# Index Page
def index(request):
    return render(request, 'posts/index.html')

# Post view
def post(request):
    
    # Get start or end points
    start = int(request.Get.get('start') or 0)
    end = int(request.Get.get('end') or (start + 9))

    # Generate post
    data = []
    for i in range(start, end + 1):
        data.append(f"Post#{i}")

    time.sleep(1)

    return JsonResponse({
        
    })