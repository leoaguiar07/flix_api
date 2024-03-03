from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    
class MovieListDetailSerializer(serializers.ModelSerializer):
    
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    

    # campo calculado (SerializerMethodField) a ser adicionado no model
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors','release_date', 'rate', 'resume' ]

     # func. que monta o valor do campo rate - deve ter o nome = get_nomedocampo
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)

        return None    

        

    '''
    def validate_release_data(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1900.")
        return value
    '''
