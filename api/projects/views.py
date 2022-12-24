from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Project


from .serializers import ProjectSerializer


class ProjectListAPIView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetailAPIView(RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
