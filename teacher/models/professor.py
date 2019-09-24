from django.db import models


class Professor(models.Model):
    """Model definition for Professor."""

    name = models.CharField(max_length=100, unique=True)
    curriculum = models.FileField(upload_to="docs/")

    class Meta:
        """Meta definition for Professor."""

        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    def __str__(self):
        """Unicode representation of Professor."""
        return self.name

