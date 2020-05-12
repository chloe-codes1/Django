from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artist, Music, Comment
from .serializers import ArtistSerializer, ArtistDetailSerializer, MusicSerializer, MusicDetailSerializer, CommentSerializer

# Create your views here.
@api_view(['GET'])
def artist_list_create(reqeust):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail_update_delete(request, artist_pk):
    # detail: GET /artists/1
    artist = get_object_or_404(Artist, id = artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET','POST'])
def music_list_create(request):
    if request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    else:
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail_update_delete(request, music_pk):
    # detail: GET /musics/1
    music = get_object_or_404(Music, id = music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, music_pk):
    # create: POST /musics/1/comment
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
        return Response(serializer.data)
    return Response({'message': 'Something went wrong!'})

@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response( {'message': 'Your comment has been updated!'})
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': 'Your comment has been successfully deleted!'})