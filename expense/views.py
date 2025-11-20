from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import date, timedelta
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))

    last_year = date.today() - timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))

    last_month = date.today() - timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))

    last_week = date.today() - timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter().values("date").order_by("date").annotate(sum=Sum("amount"))

    expense_form = ExpenseForm()
    context = {
        "expenses": expenses,
        "total_expenses": total_expenses,
        "yearly_sum": yearly_sum,
        "monthly_sum": monthly_sum,
        "weekly_sum": weekly_sum,
        "daily_sums": daily_sums,
        "expense_form": expense_form,
    }
    return render(request, "expense/index.html", context)

def edit(request, id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("expense:index")

    context = {
        "expense_form": expense_form,
    }
    return render(request, "expense/edit.html", context)

def delete(request, id):
    if request.method == "POST" and "delete" in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect("expense:index")