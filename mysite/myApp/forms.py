from django import forms
from .models import Employee

# Model Form (모델 폼)
class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'