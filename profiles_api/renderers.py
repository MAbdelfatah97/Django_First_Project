from rest_framework.renderers import BrowsableAPIRenderer
from django.utils.safestring import mark_safe

class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'image_tag':
                    data[key] = mark_safe(value)
        elif isinstance(data, list):
            for item in data:
                for key, value in item.items():
                    if key == 'image_tag':
                        item[key] = mark_safe(value)
        return super(CustomBrowsableAPIRenderer, self).render(data, accepted_media_type, renderer_context)
