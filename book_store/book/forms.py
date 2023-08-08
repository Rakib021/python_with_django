from django import forms
from book.models import BookModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model =BookModel
        fields =['id','book_name','author','genre']
