from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hospital
from .serializers import HospitalSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class CreateHosView(CreateAPIView):
    serializer_class = HospitalSerializer
#modified files
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetHosView(APIView):
    serializer_class = HospitalSerializer

    def get(self, request, *args, **kwargs):
        name_query = request.GET.get('name', None)

        if name_query:
            students = Hospital.objects.filter(name__icontains=name_query)
        else:
            students = Hospital.objects.all()

        serializer = HospitalSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateHosView(UpdateAPIView):
    serializer_class = HospitalSerializer
    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup_field)
        return get_object_or_404(Hospital, pk=pk)

    def put(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteHosView(DestroyAPIView):

    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup_field)
        return get_object_or_404(Hospital, pk=pk)

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return Response({"message": f"id {student.pk} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)