from django.shortcuts import get_object_or_404
from .serializers import AnalysisCreateSerializer, AnalysisListSerializer, AnalysisRetrieveSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models import Analysis, DefaultKeyword
from constants.models import (
  DaysOfTrendingTweets,
  NoOfPopularTweets,
  NoOfTrendingKeywords,
  NumOfTweetsPerDay,
  NumOfTweetsPerState
)
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from analysis.nlp import statewise_sentiments, get_trends
import json
from ..utils import (
  total_sentiments,
  total_indivudual_sentiments,
  get_tone_labels,
  total_sentiment_count_per_state,
  total_sentiment_count_per_date,
  max_sentiment,
  add_OR_in_strings
)
from .permissions import IsOwner

class AnaylsisView(ModelViewSet):

  queryset = Analysis.objects.all()

  serializer_action_classes = {
    'create': AnalysisCreateSerializer,
    'list': AnalysisListSerializer,
    'retrieve': AnalysisRetrieveSerializer,
  }

  permission_classes_by_action = {
    'create': [IsAuthenticated],
    'list': [IsAuthenticated],
    'retrieve': [IsAuthenticated, IsOwner],
    'destroy': [IsAuthenticated, IsOwner],
  }

  def get_queryset(self):
    user = Token.objects.filter(key=self.request.headers['Authorization'].split()[1])[0].user
    return self.queryset.filter(create_by=user)

  def get_serializer_class(self):
    return self.serializer_action_classes[self.action]

  def get_permissions(self):
    try:
      return [permission() for permission in self.permission_classes_by_action[self.action]]
    except KeyError:
      return [permission() for permission in self.permission_classes]

  def perform_create(self, serializer):
    user_referred_id = Token.objects.filter(key=self.request.headers['Authorization'].split()[1])[0].user.id
    if serializer.is_valid():
      default_keywords = DefaultKeyword.objects.all()
      num_of_tweets_per_default_keyword = NumOfTweetsPerState.objects.all()[0].value
      num_of_tweets_per_day = NumOfTweetsPerDay.objects.all()[0].value
      days_of_trending_tweets = DaysOfTrendingTweets.objects.all()[0].value
      num_of_popular_tweets = NoOfPopularTweets.objects.all()[0].value
      num_of_trending_keywords = NoOfTrendingKeywords.objects.all()[0].value
      or_def_keywords = add_OR_in_strings(default_keywords)
      or_def_keywords1 = or_def_keywords
      or_def_keywords2 = or_def_keywords

      sentiment_count_per_state = []
      for custom_keyword in self.request.data["keywords"]:
        or_def_keywords1 = or_def_keywords1 + " " + custom_keyword['keyword']
      sentiment_count_per_state.append(statewise_sentiments.state_tweets(num_of_tweets_per_default_keyword, or_def_keywords1))

      datewise_sentiments = []
      for custom_keyword in self.request.data["keywords"]:
        or_def_keywords2 = or_def_keywords2 + " " + custom_keyword['keyword']
      datewise_sentiments.append(statewise_sentiments.get_daily_tweets(or_def_keywords2, num_of_tweets_per_day, days_of_trending_tweets))

      _trending_tweets = get_trends.popular_tweets(add_OR_in_strings(default_keywords), num_of_popular_tweets)
      _trending_keywords = get_trends.trending_keywords_india(num_of_trending_keywords)

      serializer.save(
        create_by_id = user_referred_id,
        statewise_tweets = json.dumps(sentiment_count_per_state),
        datewise_tweets = json.dumps(datewise_sentiments),
        trending_tweets = json.dumps(_trending_tweets),
        trending_keywords = json.dumps(_trending_keywords),
      )

  def retrieve(self, request, pk=None):
    user_referred_id = Token.objects.filter(key=self.request.headers['Authorization'].split()[1])[0].user.id
    queryset = Analysis.objects.filter(create_by_id=user_referred_id)
    analysis = get_object_or_404(queryset, pk=pk)
    serializer = self.get_serializer(analysis)

    response = {}
    for ser_data in serializer.data:
      response[ser_data] = serializer.data[ser_data]

    default_keywords = DefaultKeyword.objects.all()
    days_of_trending_tweets = DaysOfTrendingTweets.objects.all()[0].value

    #sentiment_count_per_state = json.loads(serializer.data['statewise_tweets'])
    sentiment_count_per_state = json.loads(serializer.data['statewise_tweets'])
    datewise_sentiments = json.loads(serializer.data['datewise_tweets'])
    _total_sentiments = total_sentiments(sentiment_count_per_state)
    _total_indivudual_sentiments = total_indivudual_sentiments(sentiment_count_per_state)
    _tone_labels = get_tone_labels(sentiment_count_per_state)
    _total_sentiment_count_per_state = total_sentiment_count_per_state(sentiment_count_per_state)
    _total_sentiment_count_per_date = total_sentiment_count_per_date(datewise_sentiments)

    _max_sentiment = max_sentiment(_total_indivudual_sentiments)
    
    response['total_sentiments'] = _total_sentiments
    response['total_indivudual_sentiments'] = _total_indivudual_sentiments
    response['tone_labels'] = _tone_labels
    response['total_sentiment_count_per_state'] = _total_sentiment_count_per_state
    response['total_sentiment_count_per_date'] = _total_sentiment_count_per_date
    response['max_sentiment'] = _max_sentiment

    return Response(response)


class AnaylsisViewHome(RetrieveAPIView):

  permission_classes = [AllowAny]

  def retrieve(self, request, *args, **kwargs):
    default_keywords = DefaultKeyword.objects.all()
    num_of_tweets_per_default_keyword = NumOfTweetsPerState.objects.all()[0].value
    days_of_trending_tweets = DaysOfTrendingTweets.objects.all()[0].value
    num_of_tweets_per_day = NumOfTweetsPerDay.objects.all()[0].value
    num_of_popular_tweets = NoOfPopularTweets.objects.all()[0].value
    num_of_trending_keywords = NoOfTrendingKeywords.objects.all()[0].value
    or_def_keyword = add_OR_in_strings(default_keywords)

    sentiment_count_per_state = []
    sentiment_count_per_state.append(statewise_sentiments.state_tweets(num_of_tweets_per_default_keyword, or_def_keyword))

    datewise_sentiments = []
    datewise_sentiments.append(statewise_sentiments.get_daily_tweets(or_def_keyword, num_of_tweets_per_day, days_of_trending_tweets))

    _total_sentiments = total_sentiments(sentiment_count_per_state)
    _total_indivudual_sentiments = total_indivudual_sentiments(sentiment_count_per_state)
    _tone_labels = get_tone_labels(sentiment_count_per_state)
    _total_sentiment_count_per_state = total_sentiment_count_per_state(sentiment_count_per_state)
    _total_sentiment_count_per_date = total_sentiment_count_per_date(datewise_sentiments)

    _trending_tweets = get_trends.popular_tweets(add_OR_in_strings(default_keywords), num_of_popular_tweets)
    _trending_keywords = get_trends.trending_keywords_india(num_of_trending_keywords)

    return Response({
      'sentiment_count_per_state': sentiment_count_per_state,
      'total_sentiments': _total_sentiments,
      'total_indivudual_sentiments': _total_indivudual_sentiments,
      'tone_labels': _tone_labels,
      'total_sentiment_count_per_state': _total_sentiment_count_per_state,
      'total_sentiment_count_per_date': _total_sentiment_count_per_date,
      'trending_tweets': _trending_tweets,
      'trending_keywords': _trending_keywords
    })