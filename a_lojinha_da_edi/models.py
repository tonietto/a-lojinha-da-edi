from django.contrib.contenttypes.models import ContentType
from django.db import models


class AdminURLMixin(object):
    @models.permalink
    def get_admin_url(self):
        content_type = ContentType \
            .objects \
            .get_for_model(self.__class__)
        return ('admin:%s_%s_change' % (
            content_type.app_label,
            content_type.model), [str(self.id)])

# ˆˆˆˆˆˆˆˆˆˆAPAGAR
