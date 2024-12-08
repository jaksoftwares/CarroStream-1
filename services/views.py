from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Service
from .forms import ServiceForm

def services_page(request):
    services = Service.objects.all() 
    return render(request, 'services/services.html', {'services': services})

# View to fetch all services or a specific service
def get_services(request, pk=None):
    if pk:
        # Fetch a specific service by pk
        try:
            service = Service.objects.get(pk=pk)
            service_data = {
                'id': service.id,
                'title': service.title,
                'price': service.price,
                'description': service.description,
                'image': service.image.url if service.image else None
            }
            return JsonResponse({'status': 'success', 'service': service_data})
        except Service.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Service not found'}, status=404)
    else:
        # Fetch all services
        services = Service.objects.all()
        service_data = [
            {
                'id': service.id,
                'title': service.title,
                'price': service.price,
                'description': service.description,
                'image': service.image.url if service.image else None
            }
            for service in services
        ]
        return JsonResponse({'services': service_data})

# View to add a new service
def add_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # For file upload
        try:
            # Create a new service object
            service = Service.objects.create(
                title=title,
                price=price,
                description=description,
                image=image
            )

            # Fetch the updated list of services
            services = Service.objects.all()

            # Prepare the updated list of services to send in the response
            service_list = [
                {
                    'id': service.id,
                    'title': service.title,
                    'price': service.price
                } for service in services
            ]

            # Return success response with the updated list of services
            return JsonResponse({
                'status': 'success',
                'message': 'Service added successfully!',
                'services': service_list
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'GET':
        # Return the service details to pre-fill the form
        service_data = {
            'id': service.id,
            'title': service.title,
            'price': service.price,
            'description': service.description,
            'image': service.image.url if service.image else None
        }
        return JsonResponse({'status': 'success', 'service': service_data})

    elif request.method == 'POST':
        # Update the service with new data
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            # Return the updated service data as JSON
            updated_service = {
                'id': service.id,
                'title': service.title,
                'price': service.price,
                'description': service.description,
                'image': service.image.url if service.image else None
            }
            return JsonResponse({'status': 'success', 'message': 'Service updated successfully', 'service': updated_service})

    return JsonResponse({'status': 'error', 'message': 'Invalid data or request'})


def delete_service(request, pk):
    if request.method == 'DELETE':
        try:
            service = get_object_or_404(Service, pk=pk)
            service.delete()
            return JsonResponse({'status': 'success', 'message': 'Service deleted successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})