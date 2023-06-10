from django import forms
from .models import userMeasurements

class PostForm(forms.ModelForm):
  class Meta:
    model = userMeasurements
    fields = ('firstSize', 'secondSize')
 
  def __init__(self, *args, **kwargs):
      super(PostForm, self).__init__(*args, **kwargs)
      self.fields['firstSize'].widget.attrs.update({'class': 'formInput'})
      self.fields['secondSize'].widget.attrs.update({'class': 'formInput'})