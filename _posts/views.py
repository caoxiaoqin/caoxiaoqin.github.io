from django.contrib import auth
from django.core.paginator import Paginator
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render

from goods.forms import GoodsForm
from goods.models import GoodsCategory, Goods


def goods_category_list(request):
    if request.method == 'GET':
        categorys = GoodsCategory.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_list.html', {'categorys': categorys, 'types': types})


def goods_category_detail(request, id):
    if request.method == 'GET':
        category = GoodsCategory.objects.filter(pk=id).first()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_detail.html', {'category': category, 'types': types})
    if request.method == 'POST':
        img = request.FILES.get('category_front_image')
        if img:
            category = GoodsCategory.objects.filter(pk=id).first()
            category.category_front_image = img
            category.save()
            return HttpResponseRedirect(reverse('goods:goods_category_detail'))
        else:
            error = '图片必须上传'
            return render(request, 'goods_category_detail.html', {'error': error})


def goods_list(request):

    if request.method == 'GET':
        # TODO : 查看所有的商品信息 并在goods_list.html页面解析
        # 分页页码
        try:
            page = int(request.GET.get('page', 1))

        except Exception as e:
            page = 1
        categorys = GoodsCategory.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        paginator = Paginator(categorys, 2)
        categorys = paginator.page(page)
        return render(request, 'goods_list.html', {'categorys': categorys, 'types': types})


def goods_detail(request):
    if request.method == 'GET':
        categorys = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_detail.html', {'categorys': categorys})
    if request.method == 'POST':
        # 验证商品的信息的完整性 数据的保存
        form = GoodsForm(request.POST)
        if form.is_valid():
            # 创建
            data = form.cleaned_data
            Goods.objects.create(**data)
            return HttpResponseRedirect(reverse('goods:goods_list'))
        else:
            return render(request, 'goods_detail.html', {'errors': form.error})
