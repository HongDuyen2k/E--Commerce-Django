from django.shortcuts import redirect
from models.models import *
from django.utils.crypto import get_random_string
from django.contrib import messages

def payment_now(request):
    option = request.POST['payment']
    current_uer = request.user
    if option == 'Cash':
        carts = Cart.objects.filter(user_id=current_uer.id, status='Draft')
        for cart in carts:
            data= Cart.objects.get(id=cart.id)
            data.status = 'Done'
            data.save()
        
        order = Order.objects.get(user_id=current_uer.id, status='Draft')
        payment = Payment()
        payment.codeBill = get_random_string(length=32)
        payment.price = order.totalPriceAfter
        payment.order_id = order.id
        payment.save()

        order.status = 'Pending'
        order.save()
    messages.success(request, 'Bạn đã đặt hàng thành công')
    return redirect('general_home')