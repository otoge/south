from django.shortcuts import render
from .models import Item
from django.db.models import Q
from .forms import ProfileSearchFormSet, ProfileSearchForm
from django.shortcuts import redirect
from django.views.generic import DetailView


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
