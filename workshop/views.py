from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Workshop, Category
from .forms import WorkshopForm

def add_workshops(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form)
            form.save()
            messages.success(request, 'successfully added workshop data')
            return redirect(reverse('add_workshop'))
        else:
            messages.error(request, 'Failed to add Workshop. Please ensure that the form is valid')
    else:
        form = WorkshopForm()

    template = 'workshop/add_workshop.html'
 
    context = {
        'form': form,
    }
    return render(request, template, context)


# def edit_workshop(request, workshop_id):
#     workshop = get_object_or_404(Workshop, pk=workshop_id)
#     # print(workshop)
#     # if request.method == 'POST':
#     #     form = WorkshopForm(request.POST, request.FILES, instance=workshop)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, 'Successfully updated workshop!')
#     #         return redirect(reverse('workshop_detail', args=[workshop.id]))
#     #     else:
#     #         messages.error(request, 'Failed to update product. Please ensure the form is valid.')
#     # else:
#     form = WorkshopForm(instance=workshop)
#     messages.info(request, f'You are editing {workshop.title}')

#     template = 'workshop/edit_workshop.html'
#     context = {
#         'form': form,
#         'workshop': workshop,
#     }

#     return render(request, template, context)


def all_workshops(request):
    
    workshops = Workshop.objects.all()
    query = None
    categories = None
    template = 'workshop/workshops.html'
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            workshops = workshops.filter(category_name__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    context = {
        'workshops': workshops,
        'current_categories': categories,
    }

    return render(request, template, context)


def workshop_details(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    context = {
        'workshop': workshop
    }

    return render(request, 'workshop/workshop_detail.html', context)


def edit_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workshop!')
            return redirect(reverse('workshop_details', args=[workshop.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = WorkshopForm(instance=workshop)
    
    messages.info(request, f'You are editing {workshop.title}')
    template = 'workshop/edit_workshop.html'
    
    context = {
        'form': form,
        'workshop': workshop,
    }
    return render(request, template , context)