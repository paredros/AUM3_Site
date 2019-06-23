from django.utils.html import format_html_join
from django.conf import settings

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks

from django.shortcuts import redirect
from django.http import HttpResponse

@hooks.register('before_serve_document')
def serve_pdf(document, request):
    if document.file_extension != 'pdf':
        return  # Empty return results in the existing response
    response = HttpResponse(document.file.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename="' + document.file.name.split('/')[-1] + '"'
    if request.GET.get('download', False) in [True, 'True', 'true']:
        response['Content-Disposition'] = 'attachment; ' + response['Content-Disposition']
    return response