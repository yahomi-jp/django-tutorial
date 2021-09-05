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
  それがget_object_or_404<br>
  ```
  wake = get_object_or_404(Wake, pk=wake_id)
  ```
  オブジェクトが存在しない場合、Http404を返す


- 
# 参考 URL

[Django 公式ドキュメントのチュートリアル](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
