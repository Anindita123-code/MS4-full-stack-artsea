from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Workshop, Category
from .forms import WorkshopForm
from django.db.models import Q

from django.contrib.auth.decorators import login_required


@login_required
def add_workshops(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully added workshop data')
            return redirect(reverse('add_workshop'))
        else:
            messages.error(request,
                           'Failed to add. Please ensure that the form is valid')
    else:
        form = WorkshopForm()

    template = 'workshop/add_workshop.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def all_workshops(request): 
    workshops = Workshop.objects.all()
    _query = None
    categories = None
    template = 'workshop/workshops.html'
    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            workshops = workshops.filter(category_name__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            _query = request.GET['query']
            if not _query:
                messages.error(request, 'you didnot enter any search criteria')
                return redirect(reverse('workshops'))

            queries = Q(
                title__icontains=_query) | Q(description__icontains=_query)

            workshops = workshops.filter(queries)

    context = {
        'workshops': workshops,
        'current_categories': categories,
        'search_term': _query,
    }

    return render(request, template, context)


def workshop_details(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    context = {
        'workshop': workshop
    }

    return render(request, 'workshop/workshop_detail.html', context)


@login_required
def edit_workshop(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES, instance=workshop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workshop!')
            return redirect(reverse('workshop_details', args=[workshop.id]))
        else:
            messages.error(
                request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = WorkshopForm(instance=workshop)
    messages.info(request, f'You are editing {workshop.title}')
    template = 'workshop/edit_workshop.html' 
    context = {
        'form': form,
        'workshop': workshop,
    }
    return render(request, template, context)


@login_required
def delete_workshop(request, workshop_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only Administrator can do that')
        return redirect(reverse('home'))   
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    workshop.delete()
    messages.success(request, 'Workshop Deleted!')

    return redirect(reverse('workshops'))
