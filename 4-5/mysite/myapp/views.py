# myapp/views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Перенаправление на страницу успешного добавления продукта
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
