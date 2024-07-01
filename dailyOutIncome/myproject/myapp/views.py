from django.shortcuts import render, redirect
from .forms import TransactionForm


def my_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # 重定向到成功页面
    else:
        form = TransactionForm()
    return render(request, 'my_template.html', {'form': form})



def home(request):
    return render(request, 'home.html')


# 表格提交成功后执行的跳转
def success_view(request):
    return render(request, 'success.html')
