from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def measureApp(req):
  if req.method == 'GET':
    form = PostForm()

    return render(req, 'appIndex.html', {'form': form})
  
  elif req.method == 'POST':
    form = PostForm(req.POST)
    if form.is_valid():
      elem = form.save(commit=False)
      elem.square = float(req.POST["firstSize"]) * float(req.POST["secondSize"])
      elem.perimeter = float(req.POST["secondSize"]) * 2 + float(req.POST["secondSize"]) * 2
      elem.save()

      return render(req, 'success.html', {'elem': elem})
    
  else: return render(req, 'failed.html')