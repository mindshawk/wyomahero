from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

from .models import NewsPost

class NewsForm(forms.ModelForm):

	class Meta:
		model = NewsPost

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
		super(NewsForm, self).__init__(*args, **kwargs)