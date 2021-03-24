from django import forms
from csvsheet.models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields =['CSV_File',]