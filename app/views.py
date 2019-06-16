from django.shortcuts import render
from .models import Item, Profile, Post
from django.db.models import Q
from .forms import ProfileSearchFormSet, ProfileSearchForm
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import JsonResponse

from django_filters.views import FilterView
from .filters import ItemFilter


class ItemFilterView(FilterView):
    model = Item

    template_name = "profile_list.html"

    # queryset = Item.objects.all().order_by('name')

    filterset_class = ItemFilter
    strict = False

    paginate_by = 10

    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.GET:
            temp_item = self.request.GET.copy()
            # print(temp_item)
            # print(self.request.session['query'])
            context["get_flag"] = True
        return context
    pass


# Create your views here.
def home_page(request):
    # saved_items = Item.objects.all()
    # first_saved_item = saved_items[0]
    # line = first_saved_item.script
    # return render(request, "base.html", {"item": first_saved_item})
    profile_list = Item.objects.all()
    kensaku = False

    paginate_by = 10

    # formset = ProfileSearchFormSet(request.POST or None)
    form_object = ProfileSearchForm(request.POST or None)
    if request.method == 'POST':


        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        # formset.is_valid()
        form_object.is_valid()

        # Qオブジェクトを格納するリスト
        queries = []

        # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作っていく
        # for form in formset:
        #     # Qオブジェクトの引数になる。
        #     # {gender: 1, height__gte: 170} → Q(gender=1, height__gte=170)
        #     q_kwargs = {}
        #     # gender = form.cleaned_data.get('gender')
        #     # if gender:
        #     #     q_kwargs['gender'] = gender
        #
        #     # script = form.cleaned_data.get('script')
        #     # if script:
        #     #     q_kwargs['script'] = script
        #
        #     # progress = form.cleaned_data.get("progress")
        #     # if progress:
        #     #     q_kwargs["progress"] = progress
        #
        #     # height = form.cleaned_data.get('height')
        #     # if height:
        #     #     q_kwargs['height__gte'] = height
        #     #
        #     # weight = form.cleaned_data.get('weight')
        #     # if weight:
        #     #     q_kwargs['weight__lte'] = weight
        #
        #     # ここは、そのフォームに入力があった場合にのみ入る。
        #     # フォームが空なら、q_kwargsは空のままです。
        #     if q_kwargs:
        #         q = Q(**q_kwargs)
        #         print(q)
        #         queries.append(q)

        if queries:
            # filter(Q(...) | Q(...) | Q(...))を動的に行っている。]
            print(type(queries))
            print(queries)
            print(len(queries))
            base_query = queries.pop()
            print("aaaaaaaaaa")
            print(base_query)
            print(queries)
            for query in queries:
                print("bbbb")
                base_query |= query
                print(type(query))
                print(base_query)
            # profile_list = profile_list.filter(base_query)
        # print(formset[0].cleaned_data['script'])
        profile_list = profile_list.filter(Q(script__contains=form_object.cleaned_data['script']))
        kensaku = True

    context = {
            'profile_list': profile_list,
            'formset': form_object,
            'kensaku': kensaku,
    }

    if profile_list:
        return render(request, 'profile_list.html', context)
    else:
        if kensaku:
            print("aaaaaaaaaaaa")
            return render(request, 'profile_list.html', context)
        else:
            print("bbbbbbbb")
            return redirect("home")
        # return render(request, 'list.html', context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"


class MyView(LoginRequiredMixin, ListView):
    model = Profile
    login_url = 'accounts/login/'
    # redirect_field_name = 'home'
    template_name = "user.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user_name = self.request.user.username
        u = User.objects.get(username__exact=user_name)
        p = u.profile.scripts.all()
        print("if success")
        context["scripts"] = p
        return context


class PostList(ListView):
    model = Post
    template_name = "ajax_test.html"


def ajax_post_add(request):
    # title = request.POST.get('title')
    # post = Post.objects.create(title=title)
    user_name = request.user.username

    d = {
        'title': user_name,
    }
    return JsonResponse(d)
