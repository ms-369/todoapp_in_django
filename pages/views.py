

# Create your views here.

from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import task
import uuid

# Create your views here.

def add_task(request):
    input = task()
    try:
        if(request.method == "POST"):
            active_id=request.POST.get("task_id")
            if(active_id):
                active_task=get_object_or_404(task, id=active_id)
                active_task.desc = request.POST["todo"]
                input=active_task
                print(input.desc+".....................................")
                print(input.completed)
            else:
                input.desc = request.POST["todo"]
            input.save()
        data = {
            "tasktodo": input.desc,
            "taskcompleted": input.completed,
            "tasklist": task.objects.all,
            }
        print(data)
        return render(request,"index.html",data)
    except Exception as e:
            print("Error:", e)
            return render(request, "index.html", {"error": "An error occurred while processing your request."})
    

def delete_task(request, task_id):
     print(task_id)
     task_to_delete = get_object_or_404(task, id=task_id)
     task_to_delete.delete()
     return redirect("/")


def done_task(request, task_id):
    task_done = get_object_or_404(task, id=task_id)
    task_done.completed = True
    task_done.save()
    return redirect("/")



