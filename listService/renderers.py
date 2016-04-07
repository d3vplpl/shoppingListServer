from rest_framework import renderers


class ListWrappingJSONRenderer(renderers.JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, list):
            data = {'JSON_List': data}
            return super(ListWrappingJSONRenderer, self).render(data, accepted_media_type, renderer_context)