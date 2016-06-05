class RequestContentType:

    def process_request(self, request):
        return None

    def process_view(self, request, view_obj, *args, **kwargs):
        return None

    def process_exception(self, request):
        return None

    def process_template_response(self, request):
        return None

    def process_response(self, request, response):
        return None
