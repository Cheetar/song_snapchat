from django.conf import settings


def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_tracking_code = getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_CODE', False)
    if not settings.DEBUG and ga_tracking_code:
        return {
            'GOOGLE_ANALYTICS_TRACKING_CODE': ga_tracking_code,
        }
    return {}
