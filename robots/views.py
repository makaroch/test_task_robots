from django.http import HttpResponse, JsonResponse, FileResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .services import RobotDDO, validate_data_robot, save_new_robot, create_new_robot_report, get_report_period, \
    create_file_response


def download_robot_report(request):
    start_date, end_date = get_report_period()
    path_to_report = create_new_robot_report(
        start_date, end_date
    )
    return create_file_response(path_to_report, start_date, end_date)


@csrf_exempt
def post(request):
    try:
        robot: RobotDDO = validate_data_robot(request.POST)
        save_new_robot(robot)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Robot added successfully"}, status=201)
