from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blog
from blog.api.serializers import BlogSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
def blog_view(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    
@api_view(['PUT'])
def blog_update_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'successfully updated'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def blog_delete_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = blog.delete()
        data = {}
        if operation:
            data['success'] = 'successfully deleted'
        else:
            data['failure'] = 'delete failed'
            return Response(data=data)
        return Response(data=data)
    

@api_view(['POST'])
def blog_create_view(request):
    
    user = User.objects.get(pk=1)
    
    blog = Blog(author=user)
    
    if request.method == 'POST':
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)