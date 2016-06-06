from django.db import models
from UserApp.models import CustomizedUser
from purchaseApp.models import Portion

class AccountingModel(models.Model):
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE)
    portion = models.ForeignKey(Portion, blank=True,default=0, null=True)
    action = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # 0 = Pardakhte Pik
    # 1 = Sharzhe Hesab
    # 2 = Darkhaste Tasviye
    # 3 = Anjame Tasviye

