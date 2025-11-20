from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def index(request):
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    expenses = Expense.objects.all()
    expense_form = ExpenseForm()
    context = {
        "expenses": expenses,
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