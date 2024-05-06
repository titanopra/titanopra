from azbankgateways.exceptions import AZBankGatewaysException
import logging
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from azbankgateways import (
    bankfactories,
    models as bank_models,
    default_settings as settings,
)
from .models import Part

def shop(request):
    part = Part.objects.all()
    return render(request,'novin_part/shop.html',{'part':part})

def shop_details(request,pk):
    part = Part.objects.get(id=pk)
    partt = Part.objects.filter(id=pk)
    parts = Part.objects.all()
    return render(request,'novin_part/shop-details.html',{'part':part,'partt':partt,'parts':parts})


def finish(request):
    return render(request,'novin_part/finish.html')


def go_to_gateway_view(request,pk):
    if request.user.is_authenticated:
        part_id = Part.objects.get(id=pk)
        part_instance = Part.objects.get(id=pk)

        price = int(part_instance.price)
        amount = price

        user_mobile_number = "+989112221234"  # اختیاری


        factory = bankfactories.BankFactory()
        try:
            bank = (
                factory.auto_create()
            )
            bank.set_request(request)
            bank.set_amount(amount)
            bank.set_client_callback_url("http://localhost:8000//callback_gateway_view/")
            bank.set_mobile_number(user_mobile_number)  # اختیاری
            bank_record = bank.ready()
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            logging.critical(e)
            # TODO: redirect to failed page.
            raise e
    else:
        return redirect('acount:home')


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return render(request,'novin_part/finish.html')

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse(
        "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."
    )

def search_view(request):
    q = request.GET.get('s')
    rh = Part.objects.filter(about__icontains=q)
    return render(request, 'novin_part/shop.html', {'part': rh})
