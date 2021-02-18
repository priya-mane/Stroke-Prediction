from django.shortcuts import render, HttpResponse
from .forms import InputForm
from django.contrib import messages
from .models import User

# Create your views here.


def index(request):
    context = {}

    if (request.method == 'POST'):
        form = InputForm(request.POST)
        if form.is_valid():
            Gender = form.cleaned_data.get('Gender')
            Age = form.cleaned_data.get('Age')
            hyper_t = form.cleaned_data.get('Hypertension')
            if hyper_t == 'Yes':
                Hypertension = 1
            else:
                Hypertension = 0

            h_d = form.cleaned_data.get('Heart_disease')
            if h_d == 'Yes':
                Heart_disease = 1
            else:
                Heart_disease = 0

            Ever_married = form.cleaned_data.get('Ever_married')
            Work_type = form.cleaned_data.get('Work_type')
            Residence_type = form.cleaned_data.get('Residence_type')
            Avg_glucose_level = form.cleaned_data.get('Avg_glucose_level')
            Bmi = form.cleaned_data.get('Bmi')
            Smoking_status = form.cleaned_data.get('Smoking_status')

            user_obj = User(Gender, Age, Hypertension, Heart_disease, Ever_married,
                            Work_type, Residence_type, Avg_glucose_level, Bmi, Smoking_status)

            result, prob = user_obj.model()

            prob = prob*100

            prob = round(prob, 2)

            if result == 1:
                messages.error(
                    request, f'There is a {prob} % chance that you may have a stroke')
            else:
                messages.success(
                    request, f'There is a {prob} % chance that you may NOT have a stroke')

            context['form'] = form

    else:
        context['form'] = InputForm()
    return render(request, "index.html", context)
