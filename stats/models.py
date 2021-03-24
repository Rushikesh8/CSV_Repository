from django.db import models

# Create your models here.
sym_list =(
    ('AAPL','aapl'),
    ('AMZN','amzn'),
    ('GOOG','goog'),
    ('FB','fb'),
    ('TSLA','tsla'),
    ('BABA','baba'),
    ('TSM','tsm'),
    ('V','v'),
    ('JPM','jpm'),
    ('JNJ','jnj'),
    ('WMT','wmt'),
    ('MA','ma'),
    ('DIS','dis'),
    ('NVDA','nvda'),
    ('BAC','bac'),
    ('PG','pg'),
    ('UNH','unh'),
    ('PYPL','pypl'),
    ('HD','hd'),
    ('INTC','intc'),
    ('NFLEX','nflex'),
    ('CMCSA','cmcsa'),
    ('VZ','vz'),
    ('ADBE','adbe'),
    ('KO','ko'),
    ('CSCO','csco'),
    ('SAP','sap'),
    ('HDB','hdb'),
    ('UL','ul'),
)
class Stat(models.Model):
    serial = models.DecimalField(max_digits=2,decimal_places=0)
    symbole = models.CharField(max_length=20,choices=sym_list)
    date = models.DateField(blank=True)
    open_uni = models.DecimalField(max_digits=50,decimal_places=25)
    high = models.DecimalField(max_digits=50,decimal_places=25)
    low = models.DecimalField(max_digits=50,decimal_places=25)
    close = models.DecimalField(max_digits=50,decimal_places=25)
    volume = models.DecimalField(max_digits=50,decimal_places=25)
    adjclose = models.DecimalField(max_digits=50,decimal_places=25)

    def __str__(self):
        return self.symbole

