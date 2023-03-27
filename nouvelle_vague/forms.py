from django import forms


class AgregarMovieForm(forms.Form):
    name = forms.CharField(max_length=99)
    year = forms.IntegerField()


class AgregarUserForm(forms.Form):
    username = forms.CharField(max_length=99)
    email = forms.EmailField(max_length=99, required=True)


class AgregarRentalForm(forms.Form):
    movie = forms.CharField(max_length=99)
    days = forms.IntegerField(max_value=10)


class BuscarYearForm(forms.Form):
    year = forms.IntegerField(max_value=4)
