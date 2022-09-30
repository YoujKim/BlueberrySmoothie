from django import template
from accounts.models import Voicemark

register = template.Library()
@register.simple_tag(takes_context=True) 
def on_favs(context, voice):
    try:
        # print(context.request, voice)
        user = context.request.user
        the_list = Voicemark.objects.get_or_none(
            user=user
        )
        return voice in the_list.bookmark.all()
    except(AttributeError):
        user = context.request.user
        voicemark = Voicemark(user = context.request.user)
        voicemark.save()
        on_favs(context, voice)
