from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}: {self.email}, {self.mobile}"

class Masjid(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField( max_length=50)
    lga = models.CharField( max_length=50)
    lat_long = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="masjids_uploaded")
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} - {self.name}: {self.address}, {self.lga}, {self.lat_long}, {self.state}, {self.user_id}, {self.contact_name}, {self.contact_number} "

class MasjidsImages(models.Model):
    images = models.ImageField(upload_to='masjid_images', blank=True)
    masjid_id = models.ForeignKey(Masjid, on_delete=models.CASCADE, related_name="masjid_uploaded_mages")
    
    def __str__(self):
        return f"{self.id}, masjid ID: {self.masjid_id}"