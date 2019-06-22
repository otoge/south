import django_tables2 as tables
from .models import Profile, Item, Quote
from django.utils.html import format_html
from django.template.context_processors import csrf


class ImageColumn(tables.Column):

    # def render(self, value):
    #     return format_html('<img src="/media/img/{}.jpg" />', value)

    # def render(self, value):
    #     return format_html('''<form name="action" method="POST" value={}>
    #     <button type="submit" class="btn btn-danger" value="buttonnnn">
    #     お気に入りから削除
    #     </button>{{csrf_token}}</form>
    #     ''', value)

    # def render(self, value):
    #     csrf = '''<input
    #     type = "hidden"
    #     name = "csrfmiddlewaretoken"
    #     value = "BjGubcvG1HNaosyRSFQMDgCJjadv23PKtVis3HBkHXvalI88LzdVW41yo3RWzRnh" >
    #     '''
    #
    #
    #     text = format_html('''<form name="action" method="POST" value={}>
    #     <button type="submit" class="btn btn-danger" value="buttonnnn">
    #     お気に入りから削除
    #     </button>{"% csrf_token %"}</form>
    #     ''', value)
    #     print(text)
    #     return text

    def render(self, value):


        text = format_html('<form name="action" method="POST" value="form_v"><button type="submit" name="b_name" class="btn btn-danger" value={}>お気に入りから削除</button></form>', value)
        print(text)
        return text



class PersonTable(tables.Table):

    # staff_id = tables.Column(accessor="name.Item.script",
    #                          verbose_name="セリフ",
    #
    #                          attrs={
    #                              'td': {
    #                                  'id': "td_test",
    #                                  'class': "p_name"
    #                              }}
    #                          )

    speaker = tables.Column(accessor="get_speaker",
                            verbose_name="発言者",


                            attrs={
                                 'td': {
                                     'id': "td_test",
                                     'class': "p_name"
                                 }}
                            )

    my_extra_column = tables.Column(accessor='get_script',
                                    verbose_name='My calculated value',
                                    orderable=False
                                    )

    extra_button = ImageColumn(accessor="get_id"




    )

    class Meta:
        model = Quote
        template_name = 'django_tables2/bootstrap.html'
        fields = ["speaker", 'my_extra_column', "owner", "date_joined", "extra_button"]
