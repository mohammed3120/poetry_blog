import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
from .forms import ReportForm

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



def create_report_view(request):
    form = ReportForm(request.POST or None)
    if request.is_ajax():
        # name = request.POST.get('name')
        # remarks = request.POST.get('remarks')
        image = request.POST.get('image')
        img = get_report_image(image)
        author = Profile.objects.get(user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()
        # Report.objects.create(name=name, remarks=remarks,
        #                       image=img, author=author)
        return JsonResponse({'msg': 'send'})
    return JsonResponse({})



