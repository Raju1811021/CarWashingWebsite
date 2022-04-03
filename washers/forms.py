from django import forms
from washers import models
class registratio_form(forms.ModelForm):
    class Meta:
        model=models.Booking_Details
        fields=['name','car_no','address','mobile']
        labels={'name':'Car Owner Name','car_no':'Car No.','address':'Address','mobile':'Mobile'}
        widgets={'address':forms.Textarea(attrs={'cols':25,'rows':3})}
    def clean_car_no(self):
        data=self.cleaned_data['car_no']
        if len(data)!=4:
            raise forms.ValidationError('Car Number Must be 4 digit !')
        else:
            return data
    def clean_mobile(self):
        data=self.cleaned_data['mobile']
        if len(data)!=10:
            raise forms.ValidationError('Mobile Number Must Be 10 Digits !')
        else:
            return data