from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import RobotDDO, validate_data_robot, save_new_robot


@csrf_exempt
def add_robot(request):
    try:
        robot: RobotDDO = validate_data_robot(request.POST)
        save_new_robot(robot)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Robot added successfully"}, status=201)
