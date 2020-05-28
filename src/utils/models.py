from django.db import models

class BasicModel(models.Model):
    """Base Model."""

    created = models.DateTimeField(
            "created at",
            auto_now_add=True,
            help_text="Date time which the object was created."
    )
    modified = models.DateTimeField(
            "modifed at",
            auto_now=True,
            help_text="Date time on which the object was last modifed."
    )

    class Meta:
        """Meta options."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


