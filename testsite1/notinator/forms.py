from django import forms


class InputForm(forms.Form):
    text = forms.CharField(
        label='Input',
        max_length=3000,
        initial='Enter your text and links here',
        required=True)

    selection = forms.ChoiceField(
        choices=(('1', 'Quiz'), ('2', 'Resources')),
        label='Choose a result',
        required=True)
