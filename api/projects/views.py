from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Project


from .serializers import ProjectSerializer


class ProjectListAPIView(ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetailAPIView(RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
