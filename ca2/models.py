from django.contrib.gis.db import models


class QuietZone(models.Model):
    # Basic information
    name = models.CharField(max_length=200, help_text="Name of the quiet zone")
    description = models.TextField(help_text="Description of the quiet zone")

    # Geospatial data
    location = models.PointField(help_text="Geographic location (longitude, latitude)")

    # Quietness rating could be a decimal where lower is quieter
    noise_level = models.DecimalField(max_digits=2, decimal_places=1, help_text="Average noise level rating")

    # Amenities offered by the zone (e.g., Wi-Fi, seating, power outlets), stored as JSON
    amenities = models.JSONField(help_text="JSON structure of amenities offered", null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time this record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time this record was last updated.")

    average_rating = models.FloatField(default=0, help_text="Average user rating")
    tags = models.ManyToManyField('Tag', related_name='quiet_zones', blank=True,
                                  help_text="Tags for categorizing quiet zones")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quiet Zones"



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
