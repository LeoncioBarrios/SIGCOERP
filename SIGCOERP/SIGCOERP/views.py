from django.shortcuts import render
from django.views import View
from django.utils import timezone


class InicioView(View):
	def get(self, request, *args, **kwargs):
		fecha_actual = timezone.now()
		return render(request, 'inicio.html', {'fecha': fecha_actual})
