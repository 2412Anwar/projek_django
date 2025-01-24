from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')

def app(request):
    ar_bayar = ['EWallet', 'Bank', 'QRIS']

    # Membuat context dictionary
    context = {
        'ar_bayar': ar_bayar,
    }
    return render(request, 'app.html', context)

def process_form(request): 
    if request.method == "POST": 
        # Data form 
        nama = request.POST.get("nama") 
        email = request.POST.get("email") 
        tiket = int(request.POST.get("tiket")) 
        bayar = request.POST.get("bayar") 

        def hitung_harga(jumlah_tiket):
            harga_tiket = 200000
            if jumlah_tiket == 1:
                total_harga = harga_tiket
            elif jumlah_tiket > 1:
                total_harga = jumlah_tiket * harga_tiket * 0.9
            else:
                total_harga = 0
            return total_harga

        total_harga = hitung_harga(tiket)
        formatted_total = format_rupiah(total_harga)

        pemesanan = {
            'nama': nama,
            'email': email,
            'tiket': tiket,
            'bayar': bayar,
            'total_harga': formatted_total,
        }
        return render(request, "pemesanan.html", {"pemesanan": pemesanan})
    return render(request, "app.html")

def format_rupiah(value): 
    return f"Rp {value:,.0f}".replace(',', '.')