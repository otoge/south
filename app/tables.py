import django_tables2 as tables
from .models import Profile, Item


class PersonTable(tables.Table):

    my_extra_column = tables.Column(accessor='my_function',
                                    verbose_name='My calculated value',
                                    orderable=False
                                    )

    class Meta:
        model = Item
        template_name = 'django_tables2/bootstrap.html'
        fields = ['speaker', 'my_extra_column', "title_is"]
