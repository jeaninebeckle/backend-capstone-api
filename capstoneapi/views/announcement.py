"""View module for handling requests about announcements"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from capstoneapi.models import Announcement, JourneyUser

class AnnouncementsViewSet(ViewSet):
  """Journey Announcements"""

  def retrieve(self, request, pk=None):
    """Handle GET requests for single announcement

    returns:
      Response -- JSON serialized announcement
    """
    try:
      announcement = Announcement.objects.get(pk=pk)
      serializer = AnnouncementSerializer(announcement, context={'request': request})
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)

  def list(self, request):
    """Handle GET requests to get all announcements

    Returns:
      Response -- JSON serialized list of announcements
    """

    announcements = Announcement.objects.all()

    serializer = AnnouncementSerializer(
      announcements, many=True, context={'request': request})
    return Response(serializer.data)

  def create(self, request):
      """Handle POST operations

      Returns:
          response -- JSON serialized announcement instance
      """

      announcement = Announcement()
      announcement.content = request.data["content"]
      announcement.date = request.data["date"]
      announcement.submitter = JourneyUser.objects.get(user=request.auth.user)

      try:
        announcement.save()
        serializer = AnnouncementSerializer(announcement, context={'request': request})
        return Response(serializer.data)
      
      except ValidationError as ex:
        return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None):
      """Handle DELETE requests for a single announcement

      Returns:
          Response -- 200, 404, or 500 status code
      """
      try:
          announcement = Announcement.objects.get(pk=pk)
          announcement.delete()

          return Response({}, status=status.HTTP_204_NO_CONTENT)

      except Announcement.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

      except Exception as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnnouncementSerializer(serializers.ModelSerializer):
  """JSON Serializer for announcements

  Arguments:
    serializers
  """
  class Meta:
    model = Announcement
    fields = ('id', 'date', 'content', 'submitter')
    depth = 1
