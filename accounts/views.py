from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

#signup
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LoginForm, SignupForm
from django.urls import reverse_lazy

# my_page
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView
from .models import CustomUser

# user_update
from .forms import LoginForm, SignupForm, UserUpdateForm
from django.shortcuts import redirect, resolve_url
from django.views.generic.edit import UpdateView

# password
from .forms import LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/logout.html'
# ログアウト後は、LOGOUT_REDIRECT_URL = 'products:login'にリダイレクトするため、ログアウト用のHTMLは空でもいい


'''サインアップ'''
class Signup(CreateView):
    template_name = 'accounts/signup.html'
    form_class =SignupForm
    success_url = reverse_lazy('accounts:signup_success')

    # templateに表示するデータを追加するためオーバーライド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

    '''定義されているためオーバーライド不要
    def form_valid(self, form):
        user = form.save() # formの情報を保存
        self.object = user
        return super().form_valid(form)
    '''

'''サインアップ完了'''
class SignupDone(TemplateView):
    template_name = 'accounts/signup_success.html'

'''自分しかアクセスできないようにするMixin(共通化させるため)'''
# 詳細はQiita：https://qiita.com/kkk777/items/6f467a14b0f9616a0a79
class OnlyYouMixin(UserPassesTestMixin):
    
    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じならアクセスを許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

    # test_func関数がFalseの場合のリダイレクト先を指定
    def handle_no_permission(self):
        return redirect("report:index")


'''マイページ'''
class MyPage(OnlyYouMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/my_page.html'

'''ユーザー登録情報の更新'''
class UserUpdate(OnlyYouMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('accounts:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context


'''パスワード変更'''
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/signup.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Change Password"
        return context


'''パスワード変更完了'''
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'