from django import forms
from crispy_forms.helper import FormHelper
import re
from django.http import HttpResponse
from django.forms import ModelForm, HiddenInput
from crispy_forms.layout import Layout, Submit, Row, Column

import base64
import random
from .models import Engineer

class EngineerForm(forms.Form):
    engineersign_data = forms.CharField(widget=forms.HiddenInput())
    CUSTOMER = forms.CharField(label='', max_length=100)
    STORE = forms.CharField(label="",max_length=100)
    STORE_NO = forms.CharField(label="",max_length=100)
    CALL_OUT_NO = forms.CharField(label="",max_length=100)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "agreement_form"
        self.helper.form_method = 'post'
        super(EngineerForm, self).__init__(*args, **kwargs)

    def save(self):
        engineer_data = Engineer(
            engineersign = self.cleaned_data['engineersign_data'],
            CUSTOMER = self.cleaned_data['CUSTOMER'],
            STORE = self.cleaned_data['STORE'],
            STORE_NO = self.cleaned_data['STORE_NO'],
            CALL_OUT_NO = self.cleaned_data['CALL_OUT_NO'],

            )
        engineer_data.save()
        # print(engineer_data.id)
        return engineer_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        labels = ['CUSTOMER','STORE','STORE_NO','CALL_OUT_NO']
        for label in labels:
            self.fields[label].widget.attrs['placeholder'] = label

        # self.fields['CUSTOMER'].widget.attrs['placeholder'] = 'CUSTOMER'
        # self.fields['STORE'].widget.attrs['placeholder'] = 'STORE'
        # self.fields['STORE_NO'].widget.attrs['placeholder'] = 'STORE NO'
        # self.fields['CALL_OUT_NO'].widget.attrs['placeholder'] = 'CALL OUT NO.'




    #     self.helper.layout = Layout(
    #         Row(
    #             Column('CUSTOMER',css_class='form-group col-md-6 mb-0'),
    #             Column('CUSTOMER', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'CUSTOMER',
    #         'CUSTOMER',
    #         Row(
    #             Column('CUSTOMER', css_class='form-group col-md-6 mb-0'),
    #             Column('CUSTOMER', css_class='form-group col-md-4 mb-0'),
    #             Column('CUSTOMER', css_class='form-group col-md-2 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'CUSTOMER',
    #         Submit('submit', 'Sign in')
    #     ) 

class EngineerUpdateForm(forms.ModelForm):
    managersign_data = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = "agreement_form"
        self.helper.form_method = 'post'
        super(EngineerUpdateForm, self).__init__(*args, **kwargs)
        
        labels = ['engineersign','managersign','CUSTOMER','STORE','STORE_NO','CALL_OUT_NO']
        for label in labels:
            self.fields[label].widget=HiddenInput()
        # self.fields['CUSTOMER'].widget=HiddenInput()
        # self.fields['STORE'].widget=HiddenInput()
        # self.fields['engineersign'].widget=HiddenInput()
        # self.fields['managersign'].widget=HiddenInput()
        # self.fields['STORE_NO'].widget=HiddenInput()
        # self.fields['CALL_OUT_NO'].widget=HiddenInput()

    # def save(self):
    #     ads = Engineer(
    #         managersign = self.cleaned_data['managersign_data'],
    #         )
    #     ads.save()
    #     # print(engineer_data.id)
    #     return ads
    class Meta:
        model = Engineer
        fields = ['engineersign','CUSTOMER','STORE','STORE_NO','CALL_OUT_NO','managersign']