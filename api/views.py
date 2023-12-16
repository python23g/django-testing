from django.views import View
from django.http import HttpRequest, JsonResponse
from django.forms import model_to_dict
import json
from .models import Animal


class AnimalsView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        animals = []
        for animal in Animal.objects.all():
            animals.append(model_to_dict(animal))

        return JsonResponse({'animals': animals}, status=200)

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        if data.get('name') is None or data.get('sound') is None:
            return JsonResponse({'error': 'invalid data.'}, status=400)

        animal = Animal.objects.create(name=data['name'], sound=data['sound'])

        return JsonResponse(model_to_dict(animal), status=201)
