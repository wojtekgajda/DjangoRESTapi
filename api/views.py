from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissions) #do ustawienia w panelu admin
from rest_framework.response import Response
from api.serializers import (UserSerializer,
                             FilmSerializer,
                             AdditionalInfoSerializer,
                             ReviewSerializer,
                             ActorSerializer)

from .models import Film, Review, Actor


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    serializer_class = FilmSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'description', 'release_year']
    ordering_fields = ['id', 'title', 'release_year']
    search_fields = ['title', 'description', 'release_year']
    ordering = ['title']  # domyślny

    def get_queryset(self):
        release_year = self.request.query_params.get('release_year', None)
        id = self.request.query_params.get('id', None)

        # if id:
        #     movies = Film.objects.filter(id=id)
        # else:
        #     if release_year:
        #         movies = Film.objects.filter(release_year=release_year)
        #     else:
        #         pass
        #     movies = Film.objects.all()
        movies = Film.objects.all()
        return movies

    # def list(self, request, *args, **kwargs):
    #     movies = Film.objects.all()
    #
    #     # queryset = self.get_queryset()
    #     # title = self.request.query_params.get('title', None)
    #     # movies = Film.objects.filter(title=title)
    #     # movies = Film.objects.filter(title__icontains=title)
    #     # movies = Film.objects.filter(premier__gte='2000-01-01')
    #     # movies = Film.objects.filter(premier__year='2000')
    #     serializer = FilmSerializer(movies, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_staff:
        movie = Film.objects.create(title=request.data['title'],
                                    description=request.data['description'],
                                    after_premier=request.data['after_premier'],
                                    release_year=request.data['release_year']
                                    )
        serializer = FilmSerializer(movie, many=True)
        return Response(serializer.data)
        # else:
        # return HttpResponseNotAllowed('Not_allowed')

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.title = request.data['title']
        movie.description = request.data['description']
        movie.after_premier = request.data['after_premier']
        movie.release_year = request.data['release_year']
        movie.save()
        serializer = FilmSerializer(movie, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()
        return Response('Movie deleted')

    @action(detail=True)
    def premier(self, request, **kwargs):
        movie = self.get_object()
        movie.after_premier = False
        movie.save()

        serializer = FilmSerializer(movie, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def premier_all(self, request, **kwargs):
        movies = Film.objects.all()
        movies.update(after_premier=request.data['after_premier'])

        serializer = FilmSerializer(movies, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(methods=['POST'], detail=True)
    def connect(self, request, **kwargs):
        actor = self.get_object()
        movie = Film.objects.get(id=request.data['movie'])
        actor.movies.add(movie)

        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)
