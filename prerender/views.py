"""Views for prerendered content for SEO."""
from uuid import UUID
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
from users.models import UserProfile
from events.models import Event
from events.prioritizer import get_fresh_prioritized_events
from news.models import NewsEntry
from bodies.models import Body

def root(request):
    events = get_fresh_prioritized_events(Event.objects.all(), request)
    rendered = render_to_string('root.html', {'events': events, 'settings': settings})
    return HttpResponse(rendered)

def news(request):
    news_items = NewsEntry.objects.all()[0 : 20]
    news_items = news_items.prefetch_related('body')
    rendered = render_to_string('news.html', {'news': news_items, 'settings': settings})
    return HttpResponse(rendered)

def explore(request):
    bodies = Body.objects.all()
    rendered = render_to_string('explore.html', {'bodies': bodies, 'settings': settings})
    return HttpResponse(rendered)

def user_details(request, pk):
    try:
        UUID(pk, version=4)
        profile = get_object_or_404(UserProfile.objects, pk=pk)
    except ValueError:
        profile = get_object_or_404(UserProfile.objects, ldap_id=pk)

    if profile.profile_pic is None:
        profile.profile_pic = settings.USER_AVATAR_URL

    rendered = render_to_string('user-details.html', {'profile': profile, 'settings': settings})
    return HttpResponse(rendered)

def event_details(request, pk):
    # Prefetch
    queryset = Event.objects.prefetch_related('bodies', 'venues')

    try:
        UUID(pk, version=4)
        event = get_object_or_404(queryset, pk=pk)
    except ValueError:
        event = get_object_or_404(queryset, str_id=pk)

    rendered = render_to_string('event-details.html', {'event': event, 'settings': settings})
    return HttpResponse(rendered)

def body_details(request, pk):
    # Get queryset
    queryset = Body.objects

    try:
        UUID(pk, version=4)
        body = get_object_or_404(queryset, pk=pk)
    except ValueError:
        body = get_object_or_404(queryset, str_id=pk)

    events = get_fresh_prioritized_events(body.events, request)

    rendered = render_to_string('body-details.html', {
        'body': body,
        'settings': settings,
        'events': events,
    })
    return HttpResponse(rendered)

def body_tree(request, pk):
    body = get_object_or_404(Body.objects, pk=pk)

    rendered = render_to_string('body-tree.html', {
        'body': body,
        'settings': settings,
    })
    return HttpResponse(rendered)
