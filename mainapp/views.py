
from basketapp.models import Basket

from .models import Contact, Product, ProductCategory


def main(request):
    title = "главная"

    products = Product.objects.all()[:4]

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,

    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)


def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk),
        "basket": get_basket(request.user),
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)
