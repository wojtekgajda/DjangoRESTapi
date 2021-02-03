from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Film, AdditionalInfo, Review, Actor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # haszuje przesłane dane
        return user


class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['duration', 'type']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review', 'star_rate']
        depth = 2
        # read_only_fields = ('film', 'id')

    def update(self, instance, validated_data):
        instance.review = validated_data.get('review', instance.review)
        instance.star_rate = validated_data.get('star_rate', instance.star_rate)
        instance.save()
        return instance


class FilmSerializer(serializers.ModelSerializer):
    additional_info = AdditionalInfoSerializer(many=False)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'after_premier', 'premier', 'release_year', 'imdb_rating',
                  'additional_info', 'reviews']
        read_only_fields = ('additional_info', 'reviews',)


class FilmDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['title', 'release_year']


class ActorSerializer(serializers.ModelSerializer):
    movies = FilmDemoSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['id', 'f_name', 'l_name', 'movies']

    # Metoda stworzona do dodawania aktora razem z filmami w ktorych gra.

    # def create(self, validate_data):
    #     movies = validate_data['movies']
    #     del validate_data['movies']
    #     actor = Actor.objects.create(**validate_data)
    #
    #     for movie in movies:
    #         m = Film.objects.create(**movie)
    #         actor.movies.add(m)
    #
    #     actor.save()
    #     return actor

# class TitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Film
#         fields = ['title']
