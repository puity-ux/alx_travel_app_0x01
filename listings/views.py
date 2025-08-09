from django.http import JsonResponse

def listings_list(request):
    return JsonResponse({"message": "List of listings"})

def listing_detail(request, pk):
    return JsonResponse({"message": f"Detail of listing {pk}"})
