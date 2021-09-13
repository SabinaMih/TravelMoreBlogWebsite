from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm 



# Creating our views
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'