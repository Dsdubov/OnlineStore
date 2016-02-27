from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
# from .tasks import order_created
from cart.cart import Cart
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Order

def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    mail = order.email
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = EmailMessage(subject, message, to=[mail,])
    # mail_sent = send_mail(subject, message, 'admin@bikeshop.com', ['dubiman2011@gmail.com',])
    return mail_sent.send()

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                item['product'].quantity -= item['quantity']
                item['product'].save()
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
        else:
            print("Not valid")
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
