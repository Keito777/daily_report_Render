from django.urls import path
from .views import Login, Logout, Signup, SignupDone, MyPage,UserUpdate, PasswordChange, PasswordChangeDone

app_name = 'accounts'

urlpatterns = [
    # login, logout
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    
    # signup
    path('signup/', Signup.as_view(), name='signup'), # サインアップ
    path('signup_done/', SignupDone.as_view(), name='signup_success'), # サインアップ完了

    # my_page
    path('my_page/<int:pk>/', MyPage.as_view(), name='my_page'),
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'), # 登録情報の更新

    # password
    path('password_change/', PasswordChange.as_view(), name='password_change'), # パスワード変更
    path('password_change_done/', PasswordChangeDone.as_view(), name='password_change_done'), # パスワード変更完了
]