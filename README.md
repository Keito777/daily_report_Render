# [日報管理ツール](https://daily-report.onrender.com/)

HerokuからRenderにデプロイ環境をうつしたため、再度リポジトリを作成しました。
デプロイの流れは、以下の記事を参考に。
- [Renderにデプロイ（Django）](https://qiita.com/kkk777/items/91a00e431d3e1d72d51e)

## 作成目的
- 日々の業務内容を記録するため
- 月次報告の際、業務時間や内容を効率的に資料に記入するため

## 主な機能
- ユーザー登録、認証（サインアップ、ログイン、ログアウト機能）
- 日報の新規作成、編集、削除
- ユーザー毎に日報を管理する（他ユーザの日報は参照できない）
- ユーザー名、メールアドレス、パスワードの変更（パスワードを忘れた際に、再設定できる）
- 日報検索機能
- ページネーション機能（件ごと）

## デプロイ環境
- Render

## ライブラリ
- 詳細は、[requirements.txt](https://github.com/Keito777/daily_report_Render/blob/master/requirements.txt)を確認

## テストユーザー（確認用）
- user：test
- mail：空白
- password：testuser2000 
- アプリURL：https://daily-report.onrender.com/

## アプリの利用方法
### step1
- アクセス後、login画面が表示される
- アカウント登録を行っていない場合、「サインアップ」をクリックする
![step1](https://user-images.githubusercontent.com/65697369/197137519-6c5f3208-6b31-465e-8ac0-d8d279d2b531.png)

### step2
- ユーザー名、メールアドレス、パスワードを入力し、「Sign Up」をクリックする（アカウントが登録される）
- メールアドレスは、空白でもok
![step2](https://user-images.githubusercontent.com/65697369/197137823-a599f8b9-0f1c-4f5b-8098-013b86b11994.png)

### step3
- アカウント登録後、以下の画面が表示される
- 「Log in」をクリックするとlogin画面に移動する
![step3](https://user-images.githubusercontent.com/65697369/197145877-046750ea-e9ab-4556-bd32-07a85c418181.png)


### step4
- login画面に移動したら先ほど作成したアカウント情報を入力する
- 入力後は、「ログイン」をクリックする
![step4](https://user-images.githubusercontent.com/65697369/197146003-bce56187-c494-4809-918d-9e0d822947e7.png)


### step5
- ログインに成功した場合、以下のトップ画面が表示される
- 後は、日報の作成、または必要に応じて編集、削除を行っていく
![step5](https://user-images.githubusercontent.com/65697369/197140238-24d679ae-8775-461e-a03c-027ec3b87832.png)

### step5(日報の作成)
- 画面左上の「新規作成」をクリックすることで日報を作成することができる
![step5_create](https://user-images.githubusercontent.com/65697369/197141151-5d9e8f3f-5350-4dba-a39e-bed785902ccb.png)
- 以下の画面に移動したら、日報のタイトル、内容、作成日を入力し、「Save」をクリックする
- ナビゲーションバーの「Top」をクリックすることでトップ画面に、作成した日報が表示されたことが分かる


![create_form](https://user-images.githubusercontent.com/65697369/197143559-e122e404-4746-4be6-b7b1-1388076f7430.png)
![created](https://user-images.githubusercontent.com/65697369/197143864-cbf535c1-4dce-4ba4-a266-c7d7f252e2a9.png)


### step5(日報の修正)
- トップ画面において（上記画面）「test6」の日報をクリックする
- 以下の画面に移動したら「Edit」をクリックし、修正する
- 修正後、「Save」をクリックすることで日報を修正することができる
![update](https://user-images.githubusercontent.com/65697369/197144559-98ec9dde-ed5e-4ee1-b8a0-e12fd1b19e34.png)


### step5(日報の削除)
- トップ画面において（上記画面）「test6」の日報をクリックする
- 以下の画面に移動したら「Delete」をクリックし、削除確認画面（以下2番目の画像）に移動する
![delete](https://user-images.githubusercontent.com/65697369/197144985-6838cbff-7ef9-4b28-9ce5-71babf8d2d72.png)
- 以下の画面で「Delete」をクリックすることで日報が削除される
![delete2](https://user-images.githubusercontent.com/65697369/197145327-64c38248-104c-4082-a158-087ad4d81cc3.png)


## コード利用時の注意点(ローカル)
- セキュリティの観点からsettings.py内のSECRET_KEY環境変数の値をリポジトリ外（ローカルの.envファイル）で管理しています。
- そのため、git cloneでコードを利用する際は、Djangoのshell上でget_random_secret_key()関数を実行し、セキュリティキーを取得して、その値をSECRET_KEYに設定してからアプリを利用してください。
- デプロイ環境では、Render上でSECRET_KEY環境変数の値を設定しています。

## 今後の予定
- メールを用いたユーザー認証機能
- カレンダーを用いた日報作成日の入力機能（スーパーユーザー以外、カレンダーが表示されない問題）
- 年月別に日報を管理する機能
- カレンダーを用いた年月の検索機能

# Lisence
This project is licensed under the MIT License, see the LICENSE file for details
