from django import forms

from .models import Review

"""class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=100, error_messages={
        "required": "The text field can not be empty!!",
        "max_length": "please enter a shorter text in the text field"
    })

    review = forms.CharField(label=" Your Feedback ", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label=" Your Rating", min_value=1, max_value=5)"""


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
    # exclude= ['owner's_comment']
        labels ={
            'user_name': 'Your Name ',
            'review': 'Your Review',
            'rating': 'Your Rating'
        }
        error_messages={

            'user_name': {
                'required': 'The text field can not be empty!',
                'max_length':'please enter a shorter name '
            }


        }

