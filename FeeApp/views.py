from django.core.paginator import Paginator
from django.shortcuts import render
from .models import StudentFee, FeeInvoice
from SessionApp.models import SessionMaster

# Create your views here.
def home(request):
    
    current_session=SessionMaster.objects.values_list('id', flat=True).get(current_session=True)
    invoice_obj = FeeInvoice.objects.filter(session=current_session).order_by('-pk').all()
    paginator = Paginator(invoice_obj, 20)
    page_number = request.GET.get("page")
    invoices_list = paginator.get_page(page_number)
    return render(request, 'FeeApp/invoice_list.html',{'invoices_list':invoices_list})

def fee_details(request, invoice):
    fee_invoice = FeeInvoice.objects.filter(id=invoice).first()
    fee_detail=StudentFee.objects.filter(invoice=invoice).all()
    # return render(request, 'FeeApp/fee_details.html', {'fee_invoice':fee_invoice, 'fee_detail':fee_detail})
    return render(request, 'FeeApp/print_invoice.html', {'fee_invoice':fee_invoice, 'fee_detail':fee_detail, 'amount_word':convert_to_words(int(fee_invoice.total_amount))})

def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""  
    if num>= 1000:  
        words += ones[num // 1000] + " thousand "  
        num %= 1000  
    if num>= 100:  
        words += ones[num // 100] + " hundred "  
        num %= 100  
    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
        num = 0  
    elif num>= 20:  
        words += tens[num // 10] + " "  
        num %= 10  
    if num>= 1 and num<= 9:  
        words += ones[num] + " "  
    return words.strip()  
     
     