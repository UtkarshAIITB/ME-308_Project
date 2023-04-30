from django.http import HttpResponse
from django.shortcuts import render
from .ppb_finalised import output_func


def index(request):
    months = ["mon1", "mon2", "mon3", "mon4", "mon5", "mon6", "mon7", "mon8", "mon9", "mon10", "mon11", "mon12"]
    orders = []
    lots = []
    disect = []
    total_cost = 0
    if request.method == "POST":
        form_data = request.POST.dict()
        demand = []
        setup_cost = []
        holding_cost = 0
        for month in months:
            demand.append(float(form_data.get(f"demand-{month}")))
            setup_cost.append(float(form_data.get(f"setup-cost-{month}")))
        holding_cost = float(form_data.get("holding-cost"))
        q1 = int(form_data.get("q1"))
        q2 = int(form_data.get("q2"))
        q3 = int(form_data.get("q3"))
        d1 = float(form_data.get("d1"))
        d2 = float(form_data.get("d2"))
        d3 = float(form_data.get("d3"))
        q = [q1, q2, q3]
        d = [d1, d2, d3]
        orders, lots, disect, total_cost = output_func(demand, setup_cost, holding_cost, q, d)

    return render(request, "index.html",{"months":months, "orders": orders, "lots": lots, "disect": disect, "total_cost": total_cost})