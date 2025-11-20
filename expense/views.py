from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.
def index(request):
    expense_form = ExpenseForm()
    context = {
        "expense_form": expense_form,
    }
    return render(request, "expense/index.html", context)