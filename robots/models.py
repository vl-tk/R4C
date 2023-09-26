from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"Robot #{self.pk} {self.serial}"

    def save(self, *args, **kwargs):
        self.serial = self.model + " " + self.version
        super().save(*args, **kwargs)
