import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Base model that provides UUID and timestamp fields
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "updated_at"]
        get_latest_by = "-created_at"
