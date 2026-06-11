from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from .models import EnvironmentalObservation


def get_filtered_observations(request):
    observations = EnvironmentalObservation.objects.all()
    category = request.GET.get("category", "").strip()

    if category:
        observations = observations.filter(category=category)

    return observations


@require_GET
def observation_list(request):
    observations = get_filtered_observations(request)

    return render(
        request,
        "environmental_observations/observation_list.html",
        {
            "category": request.GET.get("category", "").strip(),
            "observations": observations,
        },
    )


@require_GET
def observation_list_api(request):
    observations = get_filtered_observations(request)

    return JsonResponse(
        {
            "count": observations.count(),
            "results": [observation.to_dict() for observation in observations],
        }
    )


@require_GET
def observation_detail_api(request, pk):
    observation = get_object_or_404(EnvironmentalObservation, pk=pk)
    return JsonResponse(observation.to_dict())
