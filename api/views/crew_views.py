from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.Crew import Crew
from ..serializers import CrewSerializer

# Create your views here.
class CrewsView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CrewSerializer
    def get(self, request):
        """Index request"""
        # Get all the Crews:
        # crews = Crew.objects.all()
        # Filter the crews by owner, so you can only see your owned crews
        crews = Crew.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CrewSerializer(crews, many=True).data
        return Response({ 'crew': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['crew']['owner'] = request.user.id
        # Serialize/create crew
        crew = CrewSerializer(data=request.data['crew'])
        # If the crew data is valid according to our serializer...
        if crew.is_valid():
            # Save the created crew & send a response
            crew.save()
            return Response({ 'crew': crew.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(crew.errors, status=status.HTTP_400_BAD_REQUEST)

class CrewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the crew to show
        crew = get_object_or_404(Crew, pk=pk)
        # Only want to show owned crews
        if request.user != crew.owner:
            raise PermissionDenied('Unauthorized, you do not own this crew')

        # Run the data through the serializer so it's formatted
        data = CrewSerializer(crew).data
        return Response({ 'crew': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate crew to delete
        crew = get_object_or_404(Crew, pk=pk)
        # Check the crew's owner against the user making this request
        if request.user != crew.owner:
            raise PermissionDenied('Unauthorized, you do not own this crew')
        # Only delete if the user owns the  crew
        crew.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate crew
        # get_object_or_404 returns a object representation of our Crew
        crew = get_object_or_404(Crew, pk=pk)
        # Check the crew's owner against the user making this request
        if request.user != crew.owner:
            raise PermissionDenied('Unauthorized, you do not own this crew')

        # Ensure the owner field is set to the current user's ID
        request.data['crew']['owner'] = request.user.id
        # Validate updates with serializer
        data = CrewSerializer(crew, data=request.data['crew'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
