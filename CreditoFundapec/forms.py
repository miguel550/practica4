from django import forms


class EstudianteForm(forms.Form):
    matricula = forms.CharField(label='Matricula', max_length=8)
    nombre = forms.CharField(label='Nombres', max_length=150)
    apellidos = forms.CharField(label='Apellidos', max_length=150)
    monto = forms.DecimalField(label='Credito', max_digits=10, decimal_places=2)

    def clean(self):
        cleaned_data = super(EstudianteForm, self).clean()
        matricula = cleaned_data.get('matricula')
        monto = cleaned_data.get('monto')
        if len(matricula) != 8:
            self.add_error('matricula', 'La matricula debe tener 8 carateres.')
        if not matricula.isdigit():
            self.add_error('matricula', 'La matricula solo debe contener numeros.')
        if len(matricula) == 8 and matricula.isdigit():
            m = int(matricula[:4])
            if 1998 > m or m > 2017:
                self.add_error('matricula', 'Matricula invalida.')
        if monto < 20000:
            self.add_error('monto', 'El monto del credito debe ser mayor o igual a RD$20,000.00')
        return cleaned_data