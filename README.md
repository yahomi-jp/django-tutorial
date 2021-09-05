# django-tutorial

<br>

# 目的

- 今までは Udemy の教材や書籍の内容を写経したり、自分の考えたアプリを作ったりしてきたが、Django 公式ドキュメントのチュートリアルをやっていなかった。
- そこで、公式のチュートリアルをやりつつ、すこしアレンジできそうなところはアレンジしてやっていくことで Django というフレームワークの理解やアプリ開発全体の理解をより深めるためにこのリポジトリを作った。<br><br>

# 気づき、学び

このドキュメントを進める上で、理解が進んだ部分や認識が変わった箇所をピックアップしていく項目<br>

- django-exten"s"ionsであり、django-exten"t"ionsではない


- 外部キーを参照する際の[AAA.BBB_id]はAAAのモデルだけを参照している（[AAA."BBB_id"]っていうイメージ）。BBBのモデルを参照して、そこからidを参照しているのではない。


- テンプレートを表示させるビュー、
  ```
    def top(request):
    wakes = Wake.objects.order_by('-id')
    template = loader.get_template('wakes/top.html')
    context = {
        'wakes': wakes
    }
    return HttpResponse(template.render(context, request))
    ```
では長いので、これを実装するためのショートカットが提供されている。<br>
それがよく使っているrender()<br>
  ```
    def top(request):
    wakes = Wake.objects.order_by('-id')
    context = {
        'wakes': wakes
    }
    return render(request, 'wakes/top.html', context)
  ```
  このビューでしっかりHttpResponseが返っている


- 以前は、```wakes = Wake.objects.all()order_by('-id')```で取得していたが、<br>```wakes = Wake.objects.order_by('-id')```でいけるっぽい。


- 特定のオブジェクトを取得、もし存在しなかった場合の例外処理を書くビューは<br>
  ```
  try:
        wake = Wake.objects.get(pk=wake_id)
    except Wake.DoesNotExist:
        raise Http404("該当するWakeがありません")
  ```
  では長い。こちらも実装するためのショートカットが提供されている。<br>
  それがget_object_or_404()<br>
  ```
  wake = get_object_or_404(Wake, pk=wake_id)
  ```
  オブジェクトが存在しない場合、Http404を返す


- request.POSTの値は常に文字列。


- try, exceptで例外処理を行う際、正常終了時に行う処理はその後のelseで記述する


- render, redirect, HttpResponseRedirectについて。
  - 関数ビューを使っているとよく目にするのがrender.
    ```return render(request, 'member.html', context)```
    contextに辞書型のオブジェクトをつっこむ。
    指定のTemplateにcontextを混ぜ込んで描画(render)する。
    userに関しては、requestに含まれているので、```{{ user.is_authenticated }}```などはcontextにuserを含ませずに実装が可能。
  
  - 訪問者をページへ飛ばすときに使うのがredirect。
    renderとは違い、そのurl先で読み込み処理を行う。
    POSTなどの情報を一度リセットしてからまっさらな状態で描画されるので、renderと使い分けることが重要。

  - HttpResponseRedirectについて。
    基本的にredirectとの差はないが、１つ大きな違いが存在する。
    それは、アプリ間を行き来することができる点である。


- editの過去形はeditedである。edittedではない汗


- テストは大事、テストのないコードは、デザインとして壊れている.
  - テストを始めるのに遅すぎるということはない。

- 

# 新しく学んだ概念、技術
- render()を使わないvanillaの実装方法
- get_object_or_404()を使わないvanillaの実装方法
- 自動テスト
  - setup_test_environment()
  - Client

# 参考 URL

[Django 公式ドキュメントのチュートリアル](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
