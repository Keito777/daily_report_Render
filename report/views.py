from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from .models import Post
from accounts.models import CustomUser

from django.db.models import Q # get_queryset()用に追加
from django.contrib import messages #　検索結果のメッセージのため追加

from .forms import CustomForm # 検索フォーム


class OwnerOnly(UserPassesTestMixin):

    # 参照条件
    def test_func(self):
        object = self.get_object()
        return object.user_name == self.request.user
    
    #def handle_no_permission(self):
        #return redirect("Detail", pk=self.kwargs["pk"])
        #return redirect("index")


class Index(LoginRequiredMixin, ListView):
    template_name = 'report/index.html'
    paginate_by = 10
    #model = Post
    #ordering = 'created' # 新規作成順　'-createdで降順'

    def get_queryset(self):
        current_user = self.request.user.username # ログイン中のユーザ名を取得（CustomUserモデルのusernameレコードの値を取得）
        user_data = CustomUser.objects.get(username=current_user) # QuerySet(条件が一致するレコードを全て取得)
        #if user_data:
        queryset = Post.objects.filter(user_name=user_data).all() # QuerySet（一致するレコード全て取得）
        queryset = queryset.order_by("created")

        # 検索フォーム
        query = self.request.GET.get('query', '') # クエリストリング(queryの値)取得
        if query:
            queryset = queryset.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
            )
        messages.add_message(self.request, messages.INFO, query)
        return queryset

class Detail(LoginRequiredMixin, OwnerOnly, DetailView):
    template_name = 'report/detaile.html'
    model = Post


class Create(LoginRequiredMixin, CreateView):
    template_name = 'report/create.html'
    form_class = CustomForm
    #model = Post # form_classは記述が多くなるのでmodelを使用
    #fields = ['title', 'body']

    def form_valid(self, form):
      '''
      フォームの保存(post)時にログインユーザをモデルに保存
      '''
      # ユーザーを投稿者として保存できるようにする
      object = form.save(commit=False) #　入力値をモデルに保存せず保留
      object.user_name = self.request.user # ログインユーザ取得
      object.save() # モデルに保存
      return super().form_valid(form)

    # idパラメータも渡す
    def get_success_url(self):
        return reverse('report:detail', kwargs={'pk': self.object.id})


class Update(LoginRequiredMixin, OwnerOnly, UpdateView):
    template_name = 'report/create.html'
    model = Post
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('report:detail', kwargs={'pk': self.object.id})

class Delete(LoginRequiredMixin, OwnerOnly, DeleteView):
    template_name = 'report/delete.html'
    model = Post
    def get_success_url(self):
        return reverse('report:index')