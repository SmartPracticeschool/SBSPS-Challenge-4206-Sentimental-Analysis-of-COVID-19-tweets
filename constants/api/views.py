from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from ..models import *
from rest_framework.permissions import IsAuthenticated

class GetAllConstantsView(RetrieveAPIView):

  permission_classes = [IsAuthenticated]

  def retrieve(self, request, *args, **kwargs):
    response = NumOfTweetsPerState.objects.all()[0].value * 36 + NumOfTweetsPerDay.objects.all()[0].value * DaysOfTrendingTweets.objects.all()[0].value + NoOfPopularTweets.objects.all()[0].value
    return Response(response)