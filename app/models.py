from django.db import models
from django.urls import reverse
# class Engineer(models.Model):
#     engineersign = models.TextField()
#     CUSTOMER = models.TextField()
#     STORE = models.TextField()


#     def __str__(self):
#     	return self.CUSTOMER



labels = ['CUSTOMER','STORE','STORE_NO','CALL_OUT_NO']

# labels = ['DISARM SYSTEM','WEIGHT','Cart NIT D/','2 Cell Batt S By Side','2Kg C02 Ref','6Kg D/Powder','Plastic Seal','Ring Pin','Ring Pin Chubb','Fire Blanket','6L Wet Chem','6L Foam Standby','6Kg D/Powder','2Kg C02 New']

class Engineer(models.Model):
	engineersign = models.TextField(blank=True,null=True)
	managersign = models.TextField(blank=True,null=True)

	def get_absolute_url(self):
		return reverse("app:detail",kwargs={"id":self.id})

for label in labels:
    Engineer.add_to_class(label, models.CharField(max_length=30,blank=True,null=True))
