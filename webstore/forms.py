from django import forms

#for learning:
# - using form class allows for easy VALIDATION, eg: 
# for the max_length below - it will not accept more than 100 
# characters within the text field: 
# if anything else enetred (not char, more than 100) it leads to the field being invalid
class PersonForm(forms.Form):
    name = forms.CharField(max_length=100,required=True, label="NAME")
    age = forms.IntegerField(label="AGE")
