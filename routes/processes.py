"""
__Seed builder__v0.2.0
  Extended module
"""

from rest_framework.decorators import action
from rest_framework.response import Response

import seed.routes.processes as SeedRoute
from domain.decimal_to_roman import decimal_roman
from domain.get_unique_chars import get_unique_chars
from seed.util.request_util import has_fields_or_400


class ProcessViewSet(SeedRoute.ProcessViewSet):

    # POST /api/processes/decimal_to_roman
    @action(detail=False, methods=['post'])
    def decimal_to_roman(self, request):
        # Validate that has required fields
        has_fields_or_400(request.data, "decimal", "user_id")
        decimal = int(request.data["decimal"])
        user_id = int(request.data["user_id"])
        decimal_roman(decimal, user_id)
        return Response(1)

    # GET /api/processes/{:id}/characters
    @action(detail=True, methods=['get'])
    def characters(self, request, pk):
        chars = get_unique_chars(pk)
        return Response(chars)
