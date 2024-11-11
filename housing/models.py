from django.db import models

class Property(models.Model):
    location = models.CharField(max_length=255)  # Location of the property
    total_sqft = models.FloatField()  # Total square footage of the property
    bhk = models.IntegerField()  # Number of bedrooms (BHK), extracted from the 'size' field
    bath = models.IntegerField()  # Number of bathrooms
    balcony = models.IntegerField()  # Number of balconies
    price = models.FloatField()  # Price in lakhs
    area_type = models.CharField(max_length=255, null=True, blank=True)  # Type of area (Super built-up, Plot, etc.)

    def __str__(self):
        return f"{self.bhk} BHK at {self.location}, {self.total_sqft} sqft"
