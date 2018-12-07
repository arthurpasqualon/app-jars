# from ipware.ip import get_real_ip

# from .models import AccessLog, AnonymousAccessLog


# class AccessLogMiddleware(object):
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not request.user.is_authenticated:
#             AnonymousAccessLog.objects.create(
#                 ip=(get_real_ip(request) or ''),
#                 user_agent=request.META.get('HTTP_USER_AGENT', ''),
#                 full_path=request.get_full_path()
#             )
#         elif not request.user.is_staff:
#             AccessLog.objects.create(
#                 user=request.user,
#                 ip=(get_real_ip(request) or ''),
#                 user_agent=request.META.get('HTTP_USER_AGENT', ''),
#                 full_path=request.get_full_path()
#             )
#         return self.get_response(request)
