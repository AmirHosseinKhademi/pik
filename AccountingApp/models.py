from django.db import models
from UserApp.models import CustomizedUser

class AccountingModel(models.Model):
    amount = models.IntegerField(default=0)
    user = models.ForeignKey(CustomizedUser)
    portion = models.ForeignKey(blank=True,default=0)
    action = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # 0 = Pardakhte Pik
    # 1 = Sharzhe Hesab
    # 2 = Darkhaste Tasviye
    # 3 = Anjame Tasviye

