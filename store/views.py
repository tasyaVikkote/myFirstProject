from django.shortcuts import render, HttpResponse
from .models import Product, Category, Comment, Addresses
from django.core import serializers

def index(req):
  if req.method == 'GET':
    products = Product.objects.all()
    categories = Category.objects.all()

    for product in products:
      product.oldPrice = int(product.price * 1.3)
    
    return render(req, 'index.html', {'products': products, 'categories': categories})

def product(req, id):
  if req.method == 'GET':
      product = Product.objects.filter(id=id).first()
      comments = Comment.objects.filter(product=product)

      product.oldPrice = int(product.price * 1.3)

      return render(req, 'product.html', {'product': product, 'comments': comments})

def contacts(req):
  if req.method == 'GET':
    addresses = Addresses.objects.all()

    return render(req, 'contacts.html', {'addresses': addresses})
  
def about(req):
  if req.method == 'GET':
    return render(req, 'about.html')

def getProductsByCategory(req):
  if req.method == 'POST':
    categoryId = req.POST['categoryId']

    category = Category.objects.filter(id=categoryId).first()
    products = []
    if categoryId == '0':
      products = Product.objects.all()
    else:
      products = Product.objects.filter(category=category)

    data = serializers.serialize('json', products)

    return HttpResponse(data, content_type='application/json')
    
def createComment(req):
  if req.method == 'POST':
    userName = req.POST['userName']
    commentText = req.POST['commentText']
    productId = req.POST['productId']

    product = Product.objects.filter(id=productId).first()

    comment = Comment(
      product=product,
      userName=userName,
      text=commentText,
    )

    comment.save()

    return HttpResponse(200)