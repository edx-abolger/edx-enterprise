"""
    Viewset for integrated_channels/v1/moodle/
"""
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ParseError

from integrated_channels.moodle.models import MoodleEnterpriseCustomerConfiguration
from .serializers import MoodleConfigSerializer


class MoodleConfigurationMixin(object):
    authentication_classes = (JwtAuthentication, SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MoodleConfigSerializer


class MoodleConfigurationViewSet(MoodleConfigurationMixin, viewsets.ModelViewSet):
    permission_required = 'enterprise.can_access_admin_dashboard'

    def get_queryset(self):
        if self.requested_enterprise_uuid is None:
            raise ParseError('Required enterprise_customer UUID is missing')

        return MoodleEnterpriseCustomerConfiguration.objects.filter(
            enterprise_customer__uuid=self.requested_enterprise_uuid
        )

    @property
    def requested_enterprise_uuid(self):
        """
        The enterprise customer uuid from request params or post body
        """
        if self.request.method in ('POST', 'PUT'):
            uuid_str = self.request.POST.get('enterprise_customer')
            if uuid_str is None:
                raise ParseError('Required enterprise_customer UUID is missing')
            return uuid_str
        else:
            uuid_str = self.request.query_params.get('enterprise_customer')
            #if validate_uuid4_string(uuid_str) is False:
            #    raise ParseError('Invalid UUID enterprise_customer_id')
            return uuid_str

    def get_permission_object(self):
        """
        Retrieve an EnterpriseCustomer uuid to do auth against
        Right now this is the same as from the request object
        meaning that only users belonging to the same enterprise
        can access these endpoints, we have to sort out the operator role use case
        """
        return self.requested_enterprise_uuid
