from django.shortcuts import render
from csvsheet.forms import CsvModelForm
from csvsheet.models import Csv
from stats.models import Stat
import csv

# Create your views here.
def upload_file(request):
    form = CsvModelForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        instance = Csv.objects.get(status=False)
        with open(instance.CSV_File.path,'r') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index == 0:
                    pass
                else:
                    serial = row[0]
                    symbole = row[1]
                    date = row[2]
                    open_uni = row[3]
                    high = row[4]
                    low = row[5]
                    close = row[6]
                    volume = row[7]
                    adjclose = row[8]
                    Stat.objects.create(
                        serial = serial,
                        symbole = symbole,
                        date = date,
                        open_uni = open_uni,
                        high = high,
                        low = low,
                        close = close,
                        volume = volume,
                        adjclose = adjclose
                    )
            instance.status = True
            instance.save()        
    return render(request,'csvsheet/index.html',context={'form':form})