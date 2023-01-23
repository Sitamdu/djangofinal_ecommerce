from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class BaseView(View):
    views = {}


class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['subcategories'] = SubCategory.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['new_products'] = Product.objects.filter(label = 'new',stock= 'In stock')
        self.views['hot_products'] = Product.objects.filter(label = 'Hot',stock= 'In stock')
        self.views['trending_products'] = Product.objects.filter(label = 'sale',stock= 'In stock')



        return render(request,'index.html',self.views)


class CategoryView(BaseView):

    def get(self,request,slug):
        ids = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = ids)
        return render(request, 'category.html', self.views)

class SearchView(BaseView):

    def get(self,request):
        query = request.GET.get('query')
        if query != '':
            self.views['search_products'] = Product.objects.filter(Q(name__icontains = query) | Q(description__icontains = query))
        # elif query != '':
        #     self.views['search_products'] = Product.objects.filter(description__icontains = query)
        else:
            return redirect('/')

        return render(request, 'search.html', self.views)


class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.views['product_detail'] = Product.objects.filter(slug=slug)
        subcat_id = Product.objects.get(slug=slug).subcategory_id
        product_id = Product.objects.get(slug=slug).id
        self.views['product_image'] = ProductImage.objects.filter(product_id = product_id)
        self.views['subcat_product'] = Product.objects.filter(subcategory_id = subcat_id)
        self.views['product_review'] = ProductReview.objects.filter(slug = slug)

        return render(request, 'single-product-normal.html', self.views)

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already taken!')
                return redirect('/signup')
            elif User.objects.filter(email= email).exists():
                messages.error(request,'The email is already taken!')
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                data.save()
                user = authenticate(username= username, password = password)
                login(request, user)
                return redirect('/')
                # return redirect('/accounts/login')   #return to login after registration.
        else:
            messages.error(request, 'Incorrect password!')
            return redirect('/signup')
    return render(request,'signup.html')

@login_required
def product_review(request,slug):
    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        comment = request.POST['comment']
        star = request.POST['star']
        x = datetime.datetime.now()
        date = str(x.strftime("%c"))
        data = ProductReview.objects.create(
            username = username,
            email = email,
            comment = comment,
            star = star,
            date = date,
            slug = slug

        )
        data.save()
    return redirect(f"/details/{slug}")

@login_required
def cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout=False).exists():
        quantity = Cart.objects.get(slug = slug,username = username,checkout=False).quantity
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        quantity = quantity+1
        if discounted_price > 0:
            original_price = quantity * discounted_price
        else:
            original_price = quantity * price

        Cart.objects.filter(slug=slug, username=username, checkout=False).update(quantity = quantity,total = original_price)
        return redirect('/my_cart')
    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        data = Cart.objects.create(
            username= username,
            slug = slug,
            total = original_price,
            items = Product.objects.filter(slug = slug)[0]
            # items = Product.objects.get(slug = slug)  dict
        )
        data.save()
        return redirect('/my_cart')

def decrease_quantity(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, username=username, checkout=False).exists():
        quantity = Cart.objects.get(slug=slug, username=username, checkout=False).quantity
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if quantity > 1:
            quantity = quantity - 1
            if discounted_price > 0:
                original_price = quantity * discounted_price
            else:
                original_price = quantity * price

            Cart.objects.filter(slug=slug, username=username, checkout=False).update(quantity=quantity,total=original_price)
            return redirect('/my_cart')
        else:
            messages.error(request,'Quantity cannot be less than 1!')
            return redirect('/my_cart')


def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug=slug, username=username, checkout=False).delete()
    messages.error(request, 'Quantity cannot be less than 1!')
    return redirect('/my_cart')



class CartView(BaseView):

    def get(self,request):
        grand_total = 0
        username = request.user.username
        self.views['my_carts'] = Cart.objects.filter(username= username,checkout = False)
        for i in self.views['my_carts']:
            grand_total = grand_total + i.total
        self.views['all_total'] = grand_total
        self.views['shipping'] = 100
        if self.views['all_total'] > 0:
            self.views['grand_total'] = grand_total + 100
        else:
            self.views['grand_total'] = 0
        self.views['cart_count'] = Cart.objects.filter(username=username, checkout=False).count()
        return render(request,'shopping-cart.html',self.views)

def wish(request,slug):
    username = request.user.username
    if Wish.objects.filter(slug = slug, username = username).exists():
        messages.error(request, 'Product is already on the wishlist!')
        return redirect('/my_wish')
    else:
        data = Wish.objects.create(
            username = username,
            slug = slug,
            items = Product.objects.filter(slug=slug)[0]
        )
        data.save()
        return redirect('/my_wish')

def delete_wish(request,slug):
    username = request.user.username
    Wish.objects.filter(slug=slug, username=username).delete()
    messages.error(request, 'The wishlist is removed!')
    return redirect('/my_wish')

class WishListView(BaseView):

    def get(self,request):
        username = request.user.username
        self.views['my_wishes'] = Wish.objects.filter(username = username)
        self.views['wish_count'] = Wish.objects.filter(username=username).count()
        return render(request,'wishlist.html',self.views)


def contact(request):
    views = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        subject = 'Thank you for messaging to our site'
        message = ' We received your message and it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['beekramrai22@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        views['mess'] = 'The message is submitted!'
        return render(request, 'contact.html',views)

    return render(request,'contact.html',views)


def checker(request,slug):
    username = request.user.username
    # Cart.objects.filter(slug= slug,username=username,checkout = True)
    return redirect('/checkout')

class CheckoutView(BaseView):
    def get(self,request):
        username = request.user.username
        self.views['my_check'] = Cart.objects.filter(username= username,checkout = False)
        return render(request, 'checkout.html', self.views)


def billing(request):
    views = {}
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipp = request.POST['zipp']
        data = Bill.objects.create(
            firstname = firstname,
            lastname = lastname,
            email = email,
            phone = phone,
            address = address,
            city = city,
            state = state,
            zipp = zipp,
        )
        data.save()
        views['mess'] ='Your order is submitted!'
        return render(request, 'checkout.html',views)

    return render(request, 'checkout.html',views)

