from .models import Task
from .serializers import TaskSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class TaskViewSet(ViewSet):
    def get(self, request):
        id = request.GET.get('id')
        if id:
            task = Task.objects.get(id=id)
            task_serializer = TaskSerializers(task)
            task.completed = True
            task.save()
            return Response(task_serializer.data)
        else:
            all_task = Task.objects.all()
            task_serializer = TaskSerializers(all_task, many=True)
            return Response(task_serializer.data)

    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        Task.objects.create(title=title, description=description)
        return Response("New Task Created")

    def put(self, request):
        task_id = request.data.get('id')
        title = request.data.get('title')
        description = request.data.get('description')

        try:
            task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response("Kindly provide correct task id")

        if title:
            task_obj.title = title

        if description:
            task_obj.description = description

        task_obj.save()

        return Response("Task Updated")


    def delete(self, request):
        task_id = request.GET.get('id')
        try:
            task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response("Kindly provide correct task id")
        task_obj.delete()
        return Response("Task Deleted")


