from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from blog.models import Post 
from .serializers import PostSerializer



# class PostDetailView(DetailView, APIView):
#     # required
#     model = Post



@api_view(['GET', 'POST'])
def post_detail(request, id):
    try:
        blog_post = Post.objects.get(id = id)
        print( blog_post)
    except :
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(blog_post)
        print()
        return Response(serializer.data)

@api_view(['PUT', ])
def post_update(request, id):
    try:
        blog_post = Post.objects.get(id = id)
        print( blog_post.__dict__)
    except :
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = PostSerializer(blog_post, data= request.data)
        data = {}
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = "updated succefully"
            return Response(data = data)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def post_delete(request, id):
    try:
        blog_post = Post.objects.get(id = id)
        print( blog_post)
    except :
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success'] = "deleted succefully"
        else:
            data ['failure'] = 'delete failed'
        return Response(data = data)

@api_view(['POST', ])
def post_create(request):
    user = User.objects.get(pk = 1)
    blog_post = Post(author=user)

    if request.method == 'POST':
        serializer = PostSerializer(blog_post, data= request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# def posts_list(request, id):
#     try:
#         blog_post = Post.objects.all()
#         print(blog_post)
#     except Post.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PostSerializer(blog_post)
#         return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def api_posts_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)