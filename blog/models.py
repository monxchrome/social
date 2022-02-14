from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class Media():
    size = models.PositiveIntegerField(_('file size'), null = True, blank=True)
    name = models.CharField(_('file name'), max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

class VideoMedia(Media):
    file = models.FileField(upload_to='videos/')

class PhotoMedia(Media):
    file = models.ImageField(upload_to='photos/')

class MediaSection(models.Model):


class Posts(models.Model):

    STATUSES = (
        (1, _('draft')),
        (2, _('on moderation')),
        (3, _('declined')),
        (3, _('published')),
    )

    TYPES = (
        (1, _('text post')),
        (2, _('photo post')),
        (3, _('video post')),
    )

    title = models.CharField(_('title'), max_length=70)
    slug = models.SlugField(editable=False, null=True, blank=True)
    status = models.PositiveSmallIntegerField(_('status')(choices=STATUSES, default=1))
    tags = models.JSONField(_('tags')(null=True, blank=True))
    type = models.PositiveSmallIntegerField(_('type')(choices=TYPES))
    content = models.TextField(_('content')(null=True, blank=True))
    views = models.PositiveIntegerField(_('views'), default=0)
    created_at = models.DateTimeField(_('created at'),(auto_now_add=True))
    published_at = models.DateTimeField(_('published at'),(null=True, blank=True))
    author = models.ForeignKey(_('author'),User, on_delete=models.CASCADE, related_name='posts')
    photo = models.OneToOneField(_('photo'),PhotoMedia, null=True, blank=True)
    video = models.OneToOneField(_('video'), VideoMedia, null=True, blank=True)