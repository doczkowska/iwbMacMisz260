
from datetime import datetime, time
from django.shortcuts import render, redirect, get_object_or_404
from service.models import Notice
from django.db.models import Q
from service.forms import SearchForm, NoticeForm
from django.contrib.auth.decorators import login_required
from private_storage.views import PrivateStorageDetailView


def list_(request):
    form = SearchForm(request.POST)
    notices = None
    if form.is_valid():
        notice_filter = Q()
        if form.cleaned_data["fraze"] != "":
            notice_filter &= Q(Q(comment__icontains=form.cleaned_data["fraze"])
                               |Q(description__icontains=form.cleaned_data["fraze"])
                               |Q(number__icontains=form.cleaned_data["fraze"]))
        if form.cleaned_data["date_from"]:
            notice_filter &= Q(date__gte=form.cleaned_data["date_from"])
        if form.cleaned_data["date_to"]:
            notice_filter &= Q(date__lte=datetime.combine(form.cleaned_data["date_to"],
                                                          time(hour=23, minute=59, second=59)))
        if form.cleaned_data["status"]:
            notice_filter &= Q(status__in=form.cleaned_data["status"])
        if form.cleaned_data["category"]:
            notice_filter &= Q(category=form.cleaned_data["category"])
        
        notices = Notice.objects.filter(notice_filter)
    return render(request,
                  template_name="service/list.html",
                  context={"date": datetime.today(),
                           "form": form,
                           "notices": notices})
    

def preview(request, pk):
    return render(request,
                  template_name="service/preview.html",
                  context={"notice": get_object_or_404(Notice,
                                                       pk=pk)})

@login_required
def create(request):
    form = NoticeForm()
    if request.POST:
        form = NoticeForm(request.POST,
                          request.FILES)
        if form.is_valid():
            form.save()
            return redirect("service-list")
        
    return render(request,
                  template_name="service/create.html",
                  context={"form": form})

@login_required
def update(request, pk):
    notice = get_object_or_404(Notice,
                               pk=pk)
    form = NoticeForm(instance=notice)
    if request.POST:
        form = NoticeForm(request.POST,
                          request.FILES,
                          instance=notice)
        if form.is_valid():
            form.save()
            return redirect("service-list")
        
    return render(request,
                  template_name="service/update.html",
                  context={"form": form})
   
@login_required
def delete(request, pk):
    get_object_or_404(Notice,
                      pk=pk).delete()
    return redirect("service-list") 

class NoticePrivateDownloadView(PrivateStorageDetailView):
    model = Notice
    model_file_filed = "file"
    
    def can_access_file(self, private_file):
        if self.request.user.is_authenticated:
            return True
        else:
            return False
