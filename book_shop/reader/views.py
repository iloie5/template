from django.shortcuts import render,redirect
from . models import Reader

# Create your views here.



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        if email:
            reader, created = Reader.objects.get_or_create(email=email)
            request.session['reader_id'] = reader.id
            return redirect('dashboard')
    return render(request, 'login.html')

def dashboard(request):
    reader_id = request.session.get('reader_id')
    if not reader_id:
        return redirect('login')
    reader = Reader.objects.get(id=reader_id)
    return render(request, 'dashboard.html', {'reader': reader})

