from django.shortcuts import get_object_or_404, render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    
    if request.method =='POST':
        form = ListForm(request.POST or None);

        if form.is_valid():
            form.save()
            # all_items = List.objects.all
            messages.success(request,('Item Has Been Added to List!'))
            # return render(request, 'home.html', {'all_items': all_items})
            return redirect('home')
            
    return render(request, 'home.html')
    
def getdata(request):
    data = List.objects.all()
    response_data = {"data": list(data.values())}
    return JsonResponse(response_data)

def delete(request, list_id):
    if request.method == 'POST':  # Ensure it's a POST request
        item = get_object_or_404(List, id=list_id)
        item.delete()
        return JsonResponse({'status': 'success', 'message': 'Item has been deleted!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def cross_off(request, list_id):
    if request.method == 'POST':  # Ensure it's a POST request
        item = get_object_or_404(List, id=list_id)
        item.completed = True
        item.save()
        return JsonResponse({'status': 'success', 'message': 'Item marked as done!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def uncross(request, list_id):
    if request.method == 'POST':  # Ensure it's a POST request
        item = get_object_or_404(List, id=list_id)
        item.completed = False
        item.save()
        return JsonResponse({'status': 'success', 'message': 'Item marked as undone!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def edit(request, list_id):
    item = List.objects.get(id=list_id)
    if request.method =='POST':
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item Has Been Edited'))
            return redirect('home') 
            # return render(request, 'edit.html', {'all_items': all_items});
    
    else:
        form = ListForm(instance = item)

    return render(request, 'edit.html',{'item': item})
