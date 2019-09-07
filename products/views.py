from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review

# Create your views here.


# All Products 
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
    
# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})
    
    
# Review List
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


# Review Detail
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})
    
    
# Add Review to Product

def add_review_to_product(request, pk):
    product = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.post = post
            product.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review_to_product.html', {'form': form})