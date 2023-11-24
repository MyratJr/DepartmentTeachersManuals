from django import forms

class Code_getter(forms.Form):
    barkod=forms.DecimalField(max_digits=300,decimal_places=0,
                        widget=forms.TextInput(attrs={
                                'class':'form-control form-control-lg',
                                'autofocus':"autofocus",
                                'placeholder':'Mugallymyň barkody',
                                'style':'''
                                    height:2cm;
                                    width:11cm;
                                    margin-left:12.5cm;
                                    border: 5px solid goldenrod;
                                    border-radius:15px
                                ''',
                            }))