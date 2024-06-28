from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



# Create your views here.
class IndexView(View):
    def get(self, request):
        #todoリストを取得
        todo_list = Task.objects.all()
        
        context = {
            "todo_list":todo_list 
        }
        
        #テンプレートをレンダリング
        return render(request, "mytodo/index.html",context)
        #return  render(request, "mytodo/index.html",context)
    
    
class AddView(View):
    def get(self, request):
        form = TaskForm()
        #テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        #登録処理
        #入力データをフォームに渡す
        form = TaskForm(request.POST)
        #入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        #データが正常であれば
        if is_valid:
            form.save()
            return redirect('/')
        
        #データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form}) 
    
class update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        
        return redirect('/')
def update_view(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, "mytodo/update.html", context)


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    

#ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
Update_task_complete = update_task_complete.as_view()



