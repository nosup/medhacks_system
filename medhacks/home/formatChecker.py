from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

class ContentTypeRestrictedFileField(FileField):

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        print("HI1\n")

        file = data.file
        try:
            print("HI2\n")

            content_type = file.content_type
            if content_type in self.content_types:
                print("HI3\n")

                if file._size > self.max_upload_size:
                    print("HI\n")
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                print("FILEtypeHI\n")

                raise forms.ValidationError(_('Only .pdf, .docx, and .jpg accepted'))
                print("WHAT")
        except AttributeError:
            pass

        return data
