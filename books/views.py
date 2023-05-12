from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer

# Create your views here.


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer


class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookSearch(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'title'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.request.query_params.get('title', '')}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)
        return obj


class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
