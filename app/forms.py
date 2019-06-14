from django import forms


class ProfileSearchForm(forms.Form):
    # gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, required=False)
    script = forms.CharField(label='セリフ', max_length='200', required=False)
    # progress = forms.IntegerField(label="進行度", required=False)
    # height = forms.FloatField(label='身長(以上)', required=False)
    # weight = forms.FloatField(label='体重(以下)', required=False)


ProfileSearchFormSet = forms.formset_factory(ProfileSearchForm)
