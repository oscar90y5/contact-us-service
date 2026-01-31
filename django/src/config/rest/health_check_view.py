from django.http import JsonResponse
from django.views import View
from django.db import connection


class HealthCheckView(View):
    def get(self, request):
        try:
            # Verificar conexión a la base de datos
            connection.ensure_connection()
            return JsonResponse({'status': 'ok'}, status=200)
        except Exception as e:
            return JsonResponse(
                {'status': 'error', 'database': str(e)},
                status=503
            )
