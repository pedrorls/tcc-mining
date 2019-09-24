from django.db import models
from teacher.models import Professor


class Word(models.Model):
    """Model definition for Word."""

    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="professor"
    )
    word = models.CharField(max_length=50)
    frequency = models.IntegerField()
    relative_frequency = models.FloatField()

    class Meta:
        """Meta definition for Word."""

        unique_together = ("professor", "word")
        verbose_name = "Word"
        verbose_name_plural = "Words"

    def __str__(self):
        """Unicode representation of Word."""
        return self.word
