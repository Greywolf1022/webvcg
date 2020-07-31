from django import forms


class FileUploadForm(forms.Form):
    scan_files = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'custom-file-input'}), label='')
