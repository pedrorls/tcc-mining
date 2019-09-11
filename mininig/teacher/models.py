from django.db import models

# Create your models here.
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


class Word(models.Model):
    """Model definition for Word."""

    word = models.CharField(max_length=50)
    frequency = models.IntegerField()
    relative_frequency = models.FloatField()

    class Meta:
        """Meta definition for Word."""

        verbose_name = "Word"
        verbose_name_plural = "Words"

    def __str__(self):
        """Unicode representation of Word."""
        return self.word


class BagOfWord(models.Model):
    """Model definition for BagOfWord."""

    professor = models.OneToOneField(
        Professor, on_delete=models.CASCADE, related_name="professor"
    )
    word = models.ManyToManyField(Word)

    class Meta:
        """Meta definition for BagOfWord."""

        verbose_name = "BagOfWord"
        verbose_name_plural = "BagOfWords"
