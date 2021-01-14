from django import forms
from service.models import Notice, Category
from django.forms.widgets import SplitDateTimeWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    user = forms.ModelChoiceField(required=False,
                                    empty_label="",
                                    label="Dla",
                                    label_suffix="",
                                    queryset=Category.objects.all(),
                                    widget=forms.widgets.Select(attrs={"class": "form-control"}))
    
    fraze = forms.CharField(required=False,
                            label="Fraza",
                            label_suffix="",
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Fraza",
                                                                  "class": "form-control",
                                                                  "style": "width:160px;"}))
    date_from = forms.DateField(required=False,
                                label="Data od",
                                label_suffix="",
                                widget=forms.widgets.DateInput(attrs={"type": "date",
                                                                      "class": "form-control"}))
    date_to = forms.DateField(required=False,
                              label="Data do",
                              label_suffix="",
                              widget=forms.widgets.DateInput(attrs={"type": "date",
                                                                    "class": "form-control"}))
    STATUS_CHOICES = [("","")] + Notice.STATUSES
    status = forms.ChoiceField(required=False,
                               label_suffix="",
                               choices=STATUS_CHOICES,
                               widget=forms.widgets.Select(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(required=False,
                                      queryset=Category.objects.all(),
                                      empty_label="",
                                      label="Kategoria",
                                      label_suffix="",
                                      widget=forms.widgets.Select(attrs={"class": "form-control"}))


class NoticeForm(forms.ModelForm):
    date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(
        date_attrs={"type": "date",
                    "class": "form-control",
                    "style": "width:160px;display:inline"},
        time_attrs={"type": "time",
                    "step":"1",
                    "class": "form-control",
                    "style": "width:160px;display:inline"}),
        label="Data"
    )
    class Meta:
        model=Notice
        fields = ["number",
                  "user",
                  "date",
                  "status",
                  "category",
                  "description",
                  "comment",
                  "image",
                  "file"]
        
        widgets = { "author": forms.widgets.Select(attrs={"class": "form-control",
                                                         "style": "width:120px;display:inline"}),
                    "date": forms.widgets.DateInput(attrs={"type": "date"}),
                    
                    "number": forms.widgets.TextInput(attrs={"class": "form-control",
                                                            "style": "width:160px;"}),
                    "status": forms.widgets.Select(attrs={"class": "form-control",
                                                         "style": "width:120px;display:inline"}),
                    "category": forms.widgets.Select(attrs={"class": "form-control",
                                                         "style": "width:200px;display:inline"}),
                    "description": forms.widgets.Textarea(attrs={"class": "form-control",
                                                                "cols": 50,
                                                                "rows": 8}),
                    "comment": forms.widgets.Textarea(attrs={"class": "form-control",
                                                            "cols": 50,
                                                            "rows": 8}),
                    "image": forms.widgets.FileInput(attrs={"class": "form-control"}),
                    "file": forms.widgets.FileInput(attrs={"class": "form-control"})}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

