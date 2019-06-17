from django.shortcuts import render
from basicforms.forms import UserForm
from basicforms.models import Users
# Create your views here.


def index(request):
    return render(request, 'basicforms/index.html')


def form_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # do something with the form
            return users(request)
    return render(request, 'basicforms/form_page.html', {'form': form})


def users(request):
    user_list = Users.objects.all()
    print(user_list)
    user_dict = {'users': user_list}
    return render(request, 'basicforms/users.html', context=user_dict)
