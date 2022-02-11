from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class Media()

class VideoMedia(models.Model):
    file = models.FileField(upload_to='videos/')

class PhotoMedia(models.Model):
    file = models.ImageField(upload_to='photos/')
    size = models.PositiveIntegerField(_('file size')(null=True, blank=True))
    name = models.CharField(_('file name'), max_length= 255, null=True, blank=True)


class Posts(models.Model):
    title = models.CharField(_('title'),max_length=70)
    slug = models.SlugField(editable=False, null=True, blank=True)

    STATUSES = (
        (1, _('draft')),
        (2, _('on moderation')),
        (3, _('declined')),
        (3, _('published')),
    )

    status = models.PositiveSmallIntegerField(_('status')(choices=STATUSES, default=1))
    tags = models.JSONField(_('tags')(null=True, blank=True))

    TYPES = (
        (1, _('text post')),
        (2, _('photo post')),
        (3, _('video post')),
    )

    type = models.PositiveSmallIntegerField(_('type')(choices=TYPES))
    content = models.TextField(_('content')(null=True, blank=True))
    views = models.PositiveIntegerField(_('views'), default=0)
    created_at = models.DateTimeField(_('created at'),(auto_now_add=True))
    published_at = models.DateTimeField(_('published at'),(null=True, blank=True))
    author = models.ForeignKey(_('author')(User, on_delete=models.CASCADE, related_name='posts'))