from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
 
app = Flask(__name__)
 
line_bot_api = LineBotApi('eDIRlU1Tf5fyzH76YfPfekkwXYMKjrSP/KB65mfZ9i72QaP4Lj7Dn+bRQd8CAK4D40bpewrWWDrtZbYLzZ5M1Wg0Q4md+CbZjpQc4iSC3+pnbX1rpvLn1Svy6pDPhrbhXsDFlSIsVq69oK9XCU7r/QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f7608a1d8c17058af7b1d4860fe39cba')
 
@app.route("/")
def test():
    return "OK"
 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
 
    return 'OK'
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    print (len([s for s in ['特定','種類','選定'] if s in event.message.text]))
#フローチャート
    if len([s for s in ['イベント','紹介'] if s in event.message.text]) >= 2:
       reply_message = "こちらはイベント紹介です！質問文に沿って回答してください！\n飼育関係のイベントの場合は\n'飼育'\nふれあい関係のイベントの場合は\n'ふれあい'\nと回答してください。"
    elif len([s for s in ['飼','育'] if s in event.message.text]) >= 2:
       reply_message = "譲渡関係のイベントの場合は\n'譲渡です'\nその他イベントの場合は\n'譲渡ではない'\nと回答してください。"
    elif len([s for s in ['譲渡','です'] if s in event.message.text]) >= 2:
       reply_message = "譲渡前関係のイベントの場合は\n'譲渡の前'\n譲渡後関係のイベントの場合は\n'譲渡の後'\nと回答してください。"
    elif len([s for s in ['譲','渡の前'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n譲渡前講習会 https://www.pref.kanagawa.jp/osirase/1594/awc/receive/workshop.html "
    elif len([s for s in ['譲','渡の後'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n譲渡後講習会 https://www.env.go.jp/nature/dobutsu/aigo/2_data/pamph/h2303b/pdf/12.pdf "
    elif len([s for s in ['譲渡','ではない'] if s in event.message.text]) >= 2:
       reply_message = "しつけ関係のイベントの場合は\n'しつけです'\nその他イベントの場合は\n'しつけではない'\nと回答してください。"
    elif len([s for s in ['しつけです','しつけです'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n犬のしつけ相談やしつけ教室・しつけのデモンストレーション\n https://www.pref.kanagawa.jp/osirase/1594/awc/owner/training.html "
    elif len([s for s in ['しつけ','ではない'] if s in event.message.text]) >= 2:
       reply_message = "職場体験関係のイベントの場合は\n'職場体験'\n動物愛護のつどい関係のイベントの場合は\n'つどい'\nと回答してください。"
    elif len([s for s in ['職場','体験'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\nインターンシップ、出張講義及び施設見学"
    elif len([s for s in ['つ','どい'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n動物愛護のつどい\n https://tumugu-project.com/activity47 "
    elif len([s for s in ['ふれ','あい'] if s in event.message.text]) >= 2:
       reply_message = "体験教室関係のイベントの場合は\n'体験教室'\nその他イベントの場合は\n'体験以外'\nと回答してください。"
    elif len([s for s in ['体験','教室'] if s in event.message.text]) >= 2:
       reply_message = "小学校低学年以下の場合は'イベントA'\nお年寄りや障害のある方の場合は'イベントB'と回答してください。"
    elif len([s for s in ['イベント','A'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n動物ふれあい教室"
    elif len([s for s in ['イベント','B'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\nコンパニオンアニマル活動"
    elif len([s for s in ['体験','以外'] if s in event.message.text]) >= 2:
       reply_message = "シャンプー・トリミング体験の場合は\n'イベントC'\n飼育体験の場合は\n'イベントD'\nと回答してください。"
    elif len([s for s in ['イベント','C'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n獣医師体験教室及びシャンプー・トリミング体験教室"
    elif len([s for s in ['イベント','D'] if s in event.message.text]) >= 2:
       reply_message = "こちらのイベントがおすすめです。\n夏休み飼育体験教室"
    elif len([s for s in ['オペレーター','おぺれーたー','と','会話','かいわ','かいは','話','オペレータ','おぺれーた','話す'] if s in event.message.text]) >= 2:
       reply_message = "オペレーターとお繋ぎしますのでしばらくお待ちください。\n営業時間内で対応を致しますので、返信まで2～3日程かかる場合がございます。予めご了承ください。\n開庁時間8時30分から17時15分 (月曜日から金曜日<祝祭日及び年末年始を除く>)"
#メイン
    elif len([s for s in ['寄付','寄附','基金','募金','献金','寄金','寄贈','した','する','浄財','送金'] if s in event.message.text]) >= 2:
        reply_message = "ありがとうございます。物品による寄附については当所から動物を引き出し、新しい飼い主を探す活動をしているボランティアも使う可能性があること、お持ち込みまたは輸送費用のご負担をご了承いただければ、寄附を受けさせていただきます。\nまた、金銭による寄附については、かながわペットのいのち基金をご検討ください。"
    elif len([s for s in ['センター','見学','自由','視察','研修','体験','研究','ガイダンス','出入り','参観'] if s in event.message.text]) >= 2:
       reply_message = "見学通路は平日の8時30分から17時15分の間、自由にご覧いただけます。\n説明等をご希望される場合は、業務に支障がない限り、希望日時に応じますので、事前に電話で予約してください（0463-58-3411）。\n団体でも個人でも受け付けています。"
    elif len([s for s in ['センター','お墓','死亡','墓石','墓地','墳墓','墓碑','霊園','事故死','病死','遺体','墓参り'] if s in event.message.text]) >= 2:
       reply_message = "お墓はありませんが、やすらぎの丘に慰霊碑があります。いつでもどなたでもお参りしていただけます。\n慰霊碑の横には、動物の遺骨を埋葬する場所があります。"
    elif len([s for s in ['センター','供養','死亡','慰霊','報恩','事故','重体','亡くなっ','埋葬','弔う','浄化','負傷'] if s in event.message.text]) >= 2:
       reply_message = "行政機関では、特定の宗教的儀式はできませんが、年に1回関係者が集まり、やすらぎの丘で動物慰霊式を行っています。"
    elif len([s for s in ['センター','ボランティア','できる','ボランテイア','ボランテア','コミュニティー','行える','図れる','役立てる','お手伝い','手伝い','手伝う'] if s in event.message.text]) >= 2:
       reply_message = "当所では、当所の事業に協力していただける方にボランティア登録をしていただき、活動していただいています。\n活動の種類は、譲渡ボランティア（団体・個人）、グルーミングボランティア（個人）及び動物愛護普及啓発ボランティア（団体・個人）になります。"
    elif len([s for s in ['センター','働く','採用','ページ','働き','雇わ','雇う','働い','社員','働き','仕事','掲載','応募'] if s in event.message.text]) >= 2:
       reply_message = "当センターは神奈川県の行政機関となります。採用については神奈川県の採用ページをご確認ください。"
    elif len([s for s in ['センター','学校','授業','いのち','教科','教育','補習','生徒','講義','カリキュラム','子ども','道徳','課外'] if s in event.message.text]) >= 2:
       reply_message = "「いのちの授業」のご依頼をお受けしております。\n【内容例】小学生向け　動物の気持ちになって考える、自分の心音を聞いていのちを感じるなど「いのちの大切さを伝える」ことに重点を置いた授業\n中学生及び高校生向け　殺処分ゼロに対する取り組みを重点的にご紹介し、動物の気持ちになって考えてもらうための授業。\nぜひお気軽にご相談ください。（0463-58-3411）"
    elif len([s for s in ['予約','センター','施設','見','でき','保護','取材','宿題','論文','ゼミ','研究','取り組み','対談','インタビュー','視察','調査'] if s in event.message.text]) >= 2:
       reply_message = "保護動物の種類や頭数、譲渡の実績等は、当所ホームページに掲載している事業概要をご確認ください。ご希望であれば、予約不要で当所の自由見学が可能です。（平日8:30～17：15）\nなお、職員への取材を希望される場合は、\n https://www.pref.kanagawa.jp/osirase/1594/awc/about/ 資料を確認していただいた上で10分程度でお願いしております。業務の都合によりお受けできない場合もありますのでご了承ください。"
    elif len([s for s in ['迷子','自宅','家','動物','居','自分','写真','犬','猫','ペット','遺棄','置き去り','逃'] if s in event.message.text]) >= 2:
       reply_message = "飼っている動物を逃がしてしまった場合は、当所（電話番号：0463-58-3411）や最寄の保健福祉事務所・警察署へご連絡ください。\nまた、当所や保健福祉事務所等へ情報提供していただいていない場合もありますので、失踪場所付近で聞き込みをしたり、失踪チラシを作成したりすることも効果があるようです。インターネット上に迷子動物等の民間掲示板がありますので、それらを利用する方法もあります。"
    elif len([s for s in ['保護','飼う','私宅','留守','飼育','お家','飼養','飼える','飼い','飼お'] if s in event.message.text]) >= 2:
       reply_message = "警察に遺失物としての届出をした後、飼い主がみつからないまま一定期間を過ぎると、自分の動物として飼うことができます。\nその後犬の場合は、お住まいの市町村に連絡して、改めて登録と狂犬病の予防注射をしてください。"
    elif len([s for s in ['犬','放し飼い','鳴き声','鳴く','鳴き','鳴い','泣き声'] if s in event.message.text]) >= 2:
       reply_message = "飼い犬の適正飼育に関する相談については、最寄りの保健福祉事務所等にご相談ください。"
    elif len([s for s in ['動物','虐待','見た','見かけた','アニマル・セラピー','屠殺','背ける','むごたらしい','観る','看る','虐殺','えげつない'] if s in event.message.text]) >= 2:
       reply_message = "動物の虐待を見かけた際、緊急の場合は警察に通報してください。\nまた、内容によっては最寄りの保健福祉事務所等や当所での対応となる場合もあります。"
    elif len([s for s in ['サル','ヘビ','ワニ','ウサギ','猿','蛇','ニシキヘビ','ネズミ','ブタ','ヤギ','トカゲ','イグアナ','飼'] if s in event.message.text]) >= 2:
       reply_message = "動物の種類によっては、飼養するための許可が必要です。\n令和2年6月1日から愛がん目的での特定動物の飼養はできません。特定動物の範囲は「特定動物を飼養している方、飼養を検討している方へ」のページをご覧ください。"
    elif len([s for s in ['ケガ','野生','怪我','けが','ストレス','犬','猫','けがし','骨折','寄生虫'] if s in event.message.text]) >= 2:
       reply_message = "病気やケガをした野生動物については、神奈川県自然環境保全センター自然保護公園部（046-248-6682）にお問い合わせください。"
    elif len([s for s in ['神奈川県','神奈川','県','かながわ','けん','野犬','野良犬','横浜','いた事','らっしゃる'] if s in event.message.text]) >= 2:
       reply_message = "現在、神奈川県内には、人からエサをもらわずに野外において集団で自活し繁殖するような、いわゆる「野犬」の生息は確認されていません。\nなお、放れて徘徊している犬を見つけたら、当所（0463-58-3411）か最寄の保健福祉事務所等にご連絡ください。"
    elif len([s for s in ['猫','室内','ネコ','ニャンコ','放し飼い','ねこ','中'] if s in event.message.text]) >= 2:
       reply_message = "猫は室内で飼うことをお勧めします。"
    elif len([s for s in ['犬','エサ','餌','えさ','ごはん','ご飯','えさやり','餌付け','給餌','ねこ','猫','良い'] if s in event.message.text]) >= 2:
       reply_message = "飼い主のいない、いわゆる野良猫にエサをあたえる行為自体は違法ではありません。\nしかし、エサをあたえることによって、猫の数が増え、その結果として周囲を汚染し、地域の生活環境を著しく損なうようなケースでは、エサをあたえていた人の責任を認めた裁判の判例があります。\nまた、エサをあたえるために他人の私有地に無断で入ることは違法になる可能性があります。"
    elif len([s for s in ['収容犬','写真','自分','撮っ','撮影','撮る','自身','自ら','私','本人','誰','子ども'] if s in event.message.text]) >= 2:
       reply_message = "すぐに、当所（0463-58-3411）に電話をしていただき、収容日、収容場所、細かい特徴などを確認してください。その結果、あなたの飼い犬である可能性がある場合は、平日の8時30分から17時15分の間に直接当所においでいただき、犬を確認してください。間違いなければ、その場で返還します。返還の際には、現金のみの返還手数料が1頭あたり1,500円、飼養管理費が1日当たり1,000円かかります。\nまた、返還時に登録と狂犬病予防注射の有無について確認させていただきますので、犬に鑑札と注射済票がついていない場合は、ご持参ください。"
    elif len([s for s in ['犬','観察札','かんさつ','取れる','札','ふだ','取れ','とっ'] if s in event.message.text]) >= 2:
       reply_message = "鑑札は首輪にぶら下げるのが一般的ですが、取れやすい場合は、鑑札を収納できる鑑札ホルダーが市販されていますので利用してください。"
    elif len([s for s in ['人','咬','犬','いぬ','噛ん','噛ま','かま','家族','飼い主','人間','ヒト','ひと'] if s in event.message.text]) >= 2:
       reply_message = "咬まれた方は、直ちに医療機関を受診してください。犬に咬まれた旨を最寄りの保健福祉事務所等に連絡してください。\nまた、人を咬んだ犬の飼い主は「飼い犬事故届出書」を提出する必要がありますので、最寄りの保健福祉事務所等に連絡してください。"
    elif len([s for s in ['動物','亡くなった','死体','亡くなっ','病死','他界','死骸','屍骸','死がい','遺体','亡骸','死後'] if s in event.message.text]) >= 2:
       reply_message = "当所では動物の死体の引取りはいたしません。市町村に動物の死体の処理を依頼する場合は各市町村にお問い合わせください。"
    elif len([s for s in ['動物','病気','獣医師','安楽死','病院','医者','かかりつけ','医院','発病','安楽','老衰','過労','心労'] if s in event.message.text]) >= 2:
       reply_message = "動物の安楽死については、公益社団法人日本獣医師会が制定した、「小動物医療の指針」において、次のように記載されています。\n11小動物医療における動物愛護と福祉\n（3）安楽死\n診療対象動物が治癒の見込みがなく、しかも苦痛を伴っている、あるいは重度の運動障害、機能障害に陥っている等、安楽死させることが動物福祉上適当であると見なされる場合には、獣医師は飼育者と十分に協議したうえで、飼育者自身の意志、決定のもとに当該動物を安楽死させることは、許容される。\n一方、その他の理由で安楽死を余儀なくされる場合もあり得るが、いずれにしても、安楽死は、最終的な選択肢として、飼育者と獣医師が十分に協議して決定すべき重要な問題である。\n日本獣医師会は、獣医師会に加入しているすべての小動物診療獣医師に対し、この「小動物医療の指針」の内容を活動指針として普及・啓発しているとのことですが、現に信条として安楽死に否定的な獣医師がいますし、獣医師会に加入していない獣医師もいます。\n指針では、安楽死処置を選択するにあたり、治療を担当した獣医師に慎重な判断を求めていますが、飼育者自身も納得ゆくよう最善の方法について双方よく話し合っていただくことが大切です。"
    elif len([s for s in ['ペットショップ','ブリーダー','選ぶ','ブリダー','ブリーダ','ペットショプ','買う','育てる','ブリーディング','プロトリマー','ペットショップペット','買え'] if s in event.message.text]) >= 2:
       reply_message = "第一種動物取扱業として、自治体への登録が義務付けられています。\n施設において、動物取扱業者名、登録番号、登録の有効期間、動物取扱責任者の氏名等の掲示が義務付けられていますので確認してみましょう。その他のポイントとして、動物の健康状態はもちろん、動物を丁寧に扱っているか、施設は清潔か、動物の知識が豊富で丁寧に説明してもらえるか、などを確認するとよいでしょう。\n販売時には、新たな飼い主に対して、品種、性別、飼育方法、関係法令、生年月日、生産地、病歴、ワクチンの接種状況、親兄弟の遺伝性疾患の発生状況等について説明し、文書を交付することが義務付けられています。\nまた、新たな飼い主探しを行う譲渡ボランティアのうち、第二種動物取扱業として自治体へ届出をしている団体もあります。\nこうしたところから動物を譲り受けることもできますので、検討されてみてはいかがでしょうか。\n当所所管地域（横浜、川崎、相模原、横須賀市を除く神奈川県内）にある動物取扱業に関する登録・届出の有無の確認、疑問や苦情につきましては、当所あて電話（0463-58-3411）でお問い合わせください。"
    elif len([s for s in ['動物','マイクロチップ','義務','どのような','守秘','使命','ナノ','義務付け','マイクロ','チップ','回路','役','やく'] if s in event.message.text]) >= 2:
       reply_message = "令和4年6月1日から、ブリーダーやペットショップ等で販売される犬や猫について、マイクロチップの装着が義務化されました。つまり、ブリーダーやペットショップ等で購入した犬や猫にはマイクロチップが装着されており、飼い主になる際には、御自身の飼い主の情報に変更する登録が必要となります。\nまた、マイクロチップが装着されていない犬や猫を拾ったり譲り受けたりし、御自身でマイクロチップを装着した場合には、飼い主の情報の登録が必要になります。"
    elif len([s for s in ['動物','飼い方','法律','民法','団体','憲法','税制','飼養','繁殖'] if s in event.message.text]) >= 2:
       reply_message = "地域における犬、猫等の動物の愛護や人に迷惑をかけない正しい飼い方などの普及啓発のために、「動物の愛護及び管理に関する法律」の第38条に基づき、神奈川県知事が委嘱した人です。"
    elif len([s for s in ['猫','ねこ','ネコ','いな','きえ','消え'] if s in event.message.text]) >= 2:
       reply_message = "猫には自分の縄張りがあるので、エサをもらえなくてもほとんど遠くへ行くことはありません。飢えてゴミを荒らしたり、家屋に侵入したりして生きていくためには何でもするので、新たな問題が発生します。"
    elif len([s for s in ['犬','お留守番','どのくらい','時間','忙しい','多忙','半日','用事','忙しく','滞在','所用','留守番','暇'] if s in event.message.text]) >= 2:
       reply_message = "犬の場合大体４．５時間です。"
    elif len([s for s in ['保護動物','譲り受ける','譲渡金','譲り受け','譲渡','給付','いくら','引き取り','貸付','金','助成','預かっ'] if s in event.message.text]) >= 2:
       reply_message = "譲渡手数料：オス4,275円 メス8,140円"
    elif len([s for s in ['譲渡適正','評価','なぜ','適性','評判','基準','公正','水準','何故','何で','どうして','なんで'] if s in event.message.text]) >= 2:
       reply_message = "収容された犬猫の健康状態、性質、大きさなど特徴はさまざまです。すべての犬猫が誰でも適正に飼養できるとは限りません。家庭動物としての適性を評価することにより、評価に応じて適正に飼養できる方とのマッチングが可能になると考えています。"
    elif len([s for s in ['犬','登録','狂犬病予防注射','飼犬','飼い犬','狂犬病','接種','緩和','ケア','会員','注射','防止'] if s in event.message.text]) >= 2:
       reply_message = "飼い犬登録について\n狂犬病予防法に基づき、生後９１日以上の犬を飼う場合は市町村に登録し、犬に鑑札をつけておかなければなりません。\n受付窓口は、以下の二通りです。生後90日を経過した飼い犬について1年に1回狂犬病予防注射が義務付けられています。\n\n① お住まいの市町の飼い犬登録の担当課。\n② 動物病院でも狂犬病予防注射と同時に行えます。"
    elif len([s for s in ['しつけ','いつ','始める','躾','しつける','はじめる','始め','始めよ','はじめれ','どんな','甘やかし','始めれ'] if s in event.message.text]) >= 2:
       reply_message = "生後2か月頃までは、母親や兄弟と共に過ごすことが大切なので、飼育を始めるのはそのあとにしましょう。生後3か月頃までの過ごし方は、その後の性格形成に影響します。本格的な散歩ができなくても、家族以外の人やほかの犬、環境に慣らしましょう。\n成犬を飼い始めるのであれば、もって生まれた気質や、これまで過ごしてきた環境を踏まえて、しつけを始めましょう。\n犬には言葉が通じないため、犬のしつけは、人の子供のしつけとは違います。"
    elif len([s for s in ['保護','迷い犬','どうなる','迷い','迷っ','守る','まよっ','護る','救う','悩む','買う','養う'] if s in event.message.text]) >= 2:
       reply_message = "保護した犬の飼い主を探すために公示(お知らせ)をします。併せてホームページに写真を掲載するなどして飼い主を探しますが、それでも飼い主が現れない場合は、新しい飼い主に譲渡します。\n犬がいなくなったら、速やかに動物愛護管理センターと近隣の警察署や交番に連絡してください。"
    elif len([s for s in ['保護','ペットショップ','とき','病気','ブリーダー','直販','経営','運営','怪我','ケガ','重病','大病','療養'] if s in event.message.text]) >= 2:
       reply_message = "保護犬猫は、保護後　獣医さんでの診察や様々な治療を受けてから募集をします。治る病気怪我は治療し、長く付き合っていく疾患やハンディ、体質はわかる範囲で、すべて明らかにして募集をいたします。ただ、残念ながら後から分かってくる疾患などもあります。\nそういったリスクも含めてすべてを受け入れていただくお心つもりが必要ではないかと思います。\n猫から人に感染する病気についての質問の場合は、「猫から人への感染」と送ってください。"
    elif len([s for s in ['愛護センター','場所','どこ','ある','何処','ドコ','ところ','営業','時間','どんな','あちこち','いったい'] if s in event.message.text]) >= 2:
       reply_message = "神奈川県動物愛護センターの住所電話番号は以下の通りです。\n〒259-1205 神奈川県平塚市土屋401\nTEL.0463-58-3411 FAX.0463-59-4931\n開庁時間：8時30分から17時15分（月曜日から金曜日〈祝祭日及び年末年始を除く〉）"
    elif len([s for s in ['餌代','いくら','かかる','餌','月','えさ','エサ','幾ら','掛かる','かかっ','掛かっ','掛る','ぐらい','くらい'] if s in event.message.text]) >= 2:
       reply_message = "種類や与える量によってかわりますが、犬・猫ともに月々4000円前後はかかります。"
#特定動物
    elif len([s for s in ['特定動物','数','種類','多く','最多','総数','多数','数種類','様々','野','さまざま','種','全部'] if s in event.message.text]) >= 2:
       reply_message = "特定動物には、約650種（ニホンザル、トラ、タカ、ワニガメ、ニシキヘビ、ワニなど）が選定されています。詳しくは以下のURLをご覧ください。\n https://www.env.go.jp/nature/dobutsu/aigo/1_law/sp-list.html "
    elif len([s for s in ['危険','動物','許可','生き物','危ない','有害','危機','恐れ','差し止める','違法','キケン','許可なく'] if s in event.message.text]) >= 2:
       reply_message = "人に危害を加えるおそれのある危険な動物とその交雑種（特定動物）は、令和2年6月1日から愛玩目的等で飼養することが禁止されました。\n動物園や試験研究施設などの特定目的で特定動物を飼う場合には、動物の種類や飼養施設ごとに都道府県知事又は政令指定都市の長の許可が必要です。"
    elif len([s for s in ['手続','手続き','動物','問い合わせ','問合せ','申し込み','申込み','申込','書類作成','問い合せ','問いあわせ','とい'] if s in event.message.text]) >= 2:
       reply_message = "手続等については、管轄の都道府県又は政令指定都市の動物愛護管理行政担当部局（権限の委任等を行っている場合を除き中核市は含みません）にお問い合わせください。https://www.env.go.jp/nature/dobutsu/aigo/3_contact/index.html "
    elif len([s for s in ['施設','構造','規模','設備','機構','中規模','小規模','敷地','団体','組織','形態','設計'] if s in event.message.text]) >= 2:
       reply_message = "飼養施設の構造や規模に関する事項は以下の通りです。\n・一定の基準を満たした「おり型施設」などで飼養保管する。\n・逸走を防止できる構造及び強度を確保する。"
    elif len([s for s in ['センター','飼養','施設','管理','飼育','運営','設備','統括','衛生','経営','一元','業務','職員'] if s in event.message.text]) >= 2:
       reply_message = "飼養施設の管理方法に関する事項は以下の通りです。\n・定期的な施設の点検を実施する。\n・第三者の接触を防止する措置をとる。\n・特定動物を飼養している旨の標識を掲示する。"
    elif len([s for s in ['動物','管理','概要','生態','とりまとめ','運営','取りまとめ','統括','会社','計画','立案','詳細'] if s in event.message.text]) >= 2:
       reply_message = "動物の管理方法に関する事項は以下の通りです。\n・施設外飼養の禁止。\n・マイクロチップ等による個体識別措置をとる（鳥類は脚環による識別も可能）。"
    elif len([s for s in ['基準','守らなかった','罰則','順守','規準','守ら','守れ','遵守','規制','規則','厳格','取り締まる'] if s in event.message.text]) >= 2:
       reply_message = "以下の行為を行った場合には、個人の場合は6ヶ月以下の懲役または100万円以下の罰金、法人の場合は5,000万円以下の罰金に処せられます。\n・無許可で特定動物を飼養または保管する。\n・不正の手段で許可を受ける。\n・特定動物の種類及び数、飼養施設の所在地、飼養施設の構造及び規模、飼養又は保管の方法、飼養又は保管が困難になった場合の対処方法等を無断で変更する。"
    elif len([s for s in ['保管','許可','申請','認可','承認','届け出','届出','許諾','許認可','提出','内諾','斡旋'] if s in event.message.text]) >= 2:
       reply_message = "特定動物飼養・保管許可申請についての詳細はこちらをご覧ください。\n https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/specific/tokuteihokankyoka.pdf "
    elif len([s for s in ['書類','ダウンロード','書面','不可欠','プリントアウト','要る','DL','作成','必用','帳票','PDF'] if s in event.message.text]) >= 2:
       reply_message = "許可申請等の書類については、以下のページで必要書類をダウンロードしてください。\n https://www.pref.kanagawa.jp/osirase/1594/awc/specific/ "
#野良猫
    elif len([s for s in ['猫','ねこ','ネコ','捕','収容','救出','護送','捕縛','搬送','送還'] if s in event.message.text]) >= 2:
       reply_message = "行政機関では、誤って飼い猫を致死処分してしまう可能性があることから、ノラ猫の捕獲は行っていません。犬の場合は、法令等により動物保護センターが捕獲・収容を行います。 \nしかし、猫には同様の規定がなく、また、所有者がいないことを確認することが困難なため、ノラ猫を捕獲し収容することはできません。 \nなお、遺棄するために捕獲した場合は100万円以下の罰金となる場合もあります。"
    elif len([s for s in ['猫','ねこ','ネコ','住み着いた','駆除','住みつい','住み着い','住み着き','住みつく','住みつき','住み着か','退治','すみつい','居着く'] if s in event.message.text]) >= 2:
       reply_message = "動物保護センター、保健福祉事務所等ではノラ猫の捕獲や駆除は行っていません。 \nノラ猫が住み着いた理由としては、柔らかい土や砂地がある、隠れる場所がある等、その猫にとって居心地がいい場所であることが考えられます。居心地を悪くすれば、その場からいなくなる可能性があります。"
    elif len([s for s in ['猫','ねこ','ネコ','子供','産んで','子ども','産ま','産まれる','産め','産まれ','赤ちゃん','産み落とす'] if s in event.message.text]) >= 2:
       reply_message = "お世話をしていた野良猫や、庭に遊びに来ていた野良猫が出産をした場合には、保護することがベストです。 \nしかし、それぞれの事情により、保護できない場合も多々あります。 その場合には、愛護センターや地元の保護団体に相談してみましょう。 たとえ、飼い主のいない野良猫でも遺棄すれば、動物愛護管理法に違反する犯罪です。"
    elif len([s for s in ['猫','ねこ','ネコ','いない','母親','実母','祖母','親','父親','なかっ','なし'] if s in event.message.text]) >= 2:
       reply_message = "母猫は、エサをとるために一時的に留守にすることがあります。\nまた、子育ての場所を変えるため、引越しの途中かもしれません。母猫 は１匹ずつしか子猫を移動できないため、残りの子猫が一時的に放置されますが、戻ってくると思われます。 母猫が戻って来ず、子猫が弱ってしまっている場合などには保護す ることもありますので、動物保護センター又はお住まいの地域の保健 福祉事務所等にご相談ください。"
    elif len([s for s in ['猫','ねこ','ネコ','路上','死んでいる','道端','道ばた','くたばる','死な','轢か','死ん','死に','道','みち'] if s in event.message.text]) >= 2:
       reply_message = "死体の処理については各市町村の清掃事業所等にご連絡ください。"
    elif len([s for s in ['猫','ねこ','ネコ','感染','病気','菌','ニャンコ','伝染','病原菌','発症','発病'] if s in event.message.text]) >= 2:
       reply_message = "猫から人に感染する病気には、猫ひっかき病、トキソプラズマ症等 様々なものがあります。\nまた、外で生活している猫の場合、室内飼養 の猫と比べ、ノミやダニが寄生している可能性は高くなります。 猫に限らず、動物を触った後は必ず手を洗ってください。体調が悪い場合には医師に相談してください。\nなお、猫エイズや猫白血病は人には感染しません。 詳細は 、厚生労働省ホームページ （ http://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/kenkou/kekkaku-kansenshou18/index.html ）をご覧ください。\n保護犬猫の病気や怪我についての質問の場合は、「保護後の病気や怪我について」と送ってください。"
    elif len([s for s in ['猫','ねこ','ネコ','保護','よいか','良い','いい','良く','飼っ','飼え','飼える','飼い','飼わ','拾'] if s in event.message.text]) >= 2:
       reply_message = "飼い主がいる可能性もありますので、動物保護センター、お住まいの地域の保健福祉事務所等、警察署に保護したことをご連絡ください。 \nなお、飼う場合は室内で飼養する等、責任をもって最期まで飼って ください。"
    elif len([s for s in ['猫','ねこ','ネコ','虐待','人','児童','家族','虐殺','いじめ'] if s in event.message.text]) >= 2:
       reply_message = "虐待を行った者は動物の愛護及び管理に関する法律により１００万 円以下の罰金が課せられます。お住まいの地域の警察署や保健福祉事務所等にご相談ください。"
    elif len([s for s in ['猫','ねこ','ネコ','去勢手術','補助制度','避妊','助成','給付','経費','手術','生殖','去勢'] if s in event.message.text]) >= 2:
       reply_message = "市町村が手術費の補助制度を設けている場合があります。詳しくはお住まいの市町村にお問い合わせください。"
    elif len([s for s in ['猫','ねこ','ネコ','庭','来ない','庭先','裏庭','ベランダ','来','追っ払っ','とびまわっ','飛び歩い'] if s in event.message.text]) >= 2:
       reply_message = "ノラ猫を来ないように対策するのは主に臭いで対策するよ方法と物で対策する方法の二つがございます。\n詳しくは（ https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/ownerless-cat/nekogaidorainn.pdf ）こちらの１２ページをご参照ください。"
    elif len([s for s in ['猫','ねこ','ネコ','対処','知り','知っ','把握','知る','調べ','教え','対策','尽くし'] if s in event.message.text]) >= 2:
       reply_message = "ノラ猫の対処方法としては、避妊または去勢手術を実施していくことで数年後には数が減っていくことが分かっているで地域の方々で協力してノラ猫の管理をしていただく必要があります。\nまたは、新しい飼い主を探すという手段もございますので詳しくは（ https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/ownerless-cat/nekogaidorainn.pdf ）の４ページから５ページをご参照ください。"
#取扱業
    elif len([s for s in ['第一種','登録','相談','面談','来所','入会','会員','斡旋','照会','紹介','飼養','飼鳥'] if s in event.message.text]) >= 2:
       reply_message = "第一種動物取扱業の相談（登録）先は、所在地ごとに異なります。\n横浜市： https://www.city.yokohama.lg.jp/kurashi/sumai-kurashi/pet-dobutsu/aigo/20110616160226.html \n川崎市： https://www.city.kawasaki.jp/350/page/0000035635.html \n相模原市： https://www.city.sagamihara.kanagawa.jp/kurashi/kenko/pet/1007500/1007506.html\n横須賀市：https://www.city.yokosuka.kanagawa.jp/3140/g_info/toriatukaigyo1.html \n上記以外の神奈川県内は神奈川県動物愛護センターで登録できます。"
    elif len([s for s in ['登録','第一種','不可欠','行う','届出','要る','会員','取扱い','取り扱い','会員','申込','取扱う'] if s in event.message.text]) >= 2:
       reply_message = "登録が必要な第一種動物取扱業については以下の通りです。\n販売・保管・貸出し・訓練・展示・競りあっせん・譲受飼養"
    elif len([s for s in ['第一種','管理','法律','取扱い','取り扱い','運営','業務','立法','税法','法令','かんり','法'] if s in event.message.text]) >= 2:
       reply_message = "第一種及び第二種動物取扱業者は省令等に則した動物の管理をしなくてはなりません。"
    elif len([s for s in ['第一種','登録','方法','取扱い','取り扱い','やり方','手順','要領','手段','手法','簡単','情報'] if s in event.message.text]) >= 2:
       reply_message = "神奈川県動物愛護センター管轄内で第一種動物取扱業を営む場合は以下の3ステップで登録する必要があります。\n\n1.都市計画法や建築基準法等の確認。\n2.必要書類の準備。\n3.事前に電話にてご予約をお願いいたします。\n※登録には5年間の有効期限があり、５年毎に更新する必要があります。また、更新登録の手数料として1件につき7,560円が必要です。\n(その他、必要書類や詳細については以下のページをご参照ください。)\n https://www.pref.kanagawa.jp/osirase/1594/awc/dealers/type1.html "
    elif len([s for s in ['更新','変更','書類','一新','改定','改編','リニューアル','改良','導入','見直し','契約','提出'] if s in event.message.text]) >= 2:
       reply_message = "その他、更新、変更時等に必要になる書類はこちらをご参照ください。\n https://www.pref.kanagawa.jp/osirase/1594/awc/dealers/type1.html "
    elif len([s for s in ['一覧','第一種','概要','詳細','に関する','取り扱う','取扱う','情報','登録簿'] if s in event.message.text]) >= 2:
       reply_message = "第一種動物取扱業者登録簿一覧は以下のものです。\n https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/dealers/type1/tourokubo.pdf "
    elif len([s for s in ['第一種','第二種','違い','登録','相違','違う','異なる','差異','違っ','食い違い','異なっ'] if s in event.message.text]) >= 2:
       reply_message = "第一種動物取扱業の登録が必要なのは、営利を目的として動物の取扱業を営む場合です。\n第二種動物取扱業の届出が必要なのは、営利を目的とせずに専用の飼養施設を設けて一定数以上の動物を業として取り扱う場合です。"
    elif len([s for s in ['第二種','第二種とは','何','使命','促進','趣旨','責任','いったい','一体','なに','なにか','にあたって'] if s in event.message.text]) >= 2:
       reply_message = "第二種動物取扱業とは、非営利目的で、専用の飼養施設を設けて一定数以上の動物を業として取り扱う活動を指します。\n動物の愛護及び管理に関する法律の改正により、新たに設けられました。\n動物愛護団体の動物シェルターや公園等での非営利の展示などが対象とされ、非営利の活動であり、人との居住部と区分できる飼養施設を有し、一定以上の飼養頭数を飼養している場合は、第二種動物取扱業に該当します。\n当所の管轄地域は神奈川県内の横浜市、川崎市、相模原市及び横須賀市を除く地域になります。"
    elif len([s for s in ['動物取扱業者','基準','法令','規準','査定','法律','業法','法規','規範','規則','規定','順守'] if s in event.message.text]) >= 2:
       reply_message = "こちらの「第一種動物取扱業者及び第二種動物取扱業者が取り扱う動物の管理の方法等の基準を定める省令等について」をご覧ください。\n https://www.pref.kanagawa.jp/osirase/1594/awc/dealers/type2.html "
    elif len([s for s in ['第二種','届出','書類','必要','届け出','取り扱い','届出る','備置','届け出る','申告','帳簿','業務','事務'] if s in event.message.text]) >= 2:
       reply_message = "第二動物取扱業の届出は、業種別、飼養施設の所在地ごとになっており、必要書類は以下の7枚です。\n\n1.第二種動物取扱業届出書\n2.飼養施設の平面図、付近の見取図\n3.ケージ等の規模を示す平面図・立面図\n4.飼養施設の土地及び建物について必要な権原を有することを証明する書類\n5.第二種動物取扱業の実施の方法\n6.登記事項証明書\n7.役員の氏名及び住所以下URLの「第二種動物取扱業の届出の手続き」から入手が可能です。\n https://www.pref.kanagawa.jp/osirase/1594/awc/dealers/type2.html "
    elif len([s for s in ['第二種','手数','金','仲介','取引','経費','額','資本','代金','資金','礼金','料'] if s in event.message.text]) >= 2:
       reply_message = "手数料は無料です。"
    elif len([s for s in ['第二種','飼育頭数','頭数','取扱い','取り扱い','飼養','数','員数','頭','とう','すう','かず'] if s in event.message.text]) >= 2:
       reply_message = "第二動物取扱業の飼育頭数はこちらになります。\n大型動物の場合：哺乳類・鳥類・特定動物が3頭以上。\n中型動物の場合：哺乳類・鳥類・爬虫類が10頭以上。\n小型動物の場合：哺乳類・鳥類・爬虫類が50頭以上。\n対象動物のより詳細な情報については、こちらをご覧ください。\n https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/dealers/type2/621385.pdf "
    elif len([s for s in ['動物取扱責任者研修','責任者','研修','主任','セキニン','講習','教育','養成','実習','視察','なすり合い','転嫁'] if s in event.message.text]) >= 2:
       reply_message = "動物取扱責任者研修は、動物取扱責任者の業務に必要な知識及び能力に関する研修です。\n動物の愛護及び管理に関する法律第22条第３項及び同法施行規則第10条第３項において、第一種動物取扱業者は、選任したすべての動物取扱責任者に、動物取扱責任者研修を受けさせなければならないとされています。\n以下の書類をご確認ください。\n・https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/dealers/type1/221117_kennsyuu.pdf\n・https://www.pref.kanagawa.jp/osirase/1594/awc/assets/pdf/dealers/type1/221117_annai.pdf\n※本県の研修を受講できない場合は、横浜市、川崎市、相模原市及び横須賀市で開催される研修会の受講も可能ですが、詳細は各市にお問い合わせください。"
    elif len([s for s in ['家畜伝染病予防法','予防','対象','伝染病','感染','病気','疫病','感染','蔓延','まん延','接種','防ぐ'] if s in event.message.text]) >= 2:
       reply_message = "対象動物は、牛・水牛・鹿・馬・めん羊・山羊・豚・いのしし・鶏・あひる・うずら・きじ・だちょう・ほろほろ鳥及び七面鳥になります。\n詳しくは、家畜を飼養する地域を管轄する家畜保健衛生所にご相談ください。\n地域ごとの家畜保健衛生所はこちらです。\n県央家畜保健衛生所： https://www.pref.kanagawa.jp/docs/cf5/index.html \n湘南家畜保健衛生所： http://www.pref.kanagawa.jp/docs/gz4/index.html "
    elif len([s for s in ['感染防止対策取組書','LINE','お知らせ','ウイルス','細菌','メール','おしらせ','スマホアプリ','アプリ','アプリケーション','伝染','まん延'] if s in event.message.text]) >= 2:
       reply_message = "「感染防止対策取組書」とは、事業所（店舗など）で取り組むコロナ感染防止の対策が一覧で分かるものです。\n県が発行をしております。\n詳細は以下のURLからご確認ください。\n https://www.pref.kanagawa.jp/docs/ga4/corona/osirase.html "
    elif len([s for s in ['Bウイルス','患者','発生','ウィルス','感染','病原菌','ワクチン','発症','発病','細菌','菌','はっせい'] if s in event.message.text]) >= 2:
       reply_message = "Bウイルス病（四類感染症）はマカク属のサルとの直接的な接触（咬傷、擦過傷）により感染するとされています。今般、鹿児島市内で、実験サル取扱施設の従事者がBウイルス病を発症した事例がありましたので、情報提供を致します。\n従事している実験サル取扱施設内での感染が推定されているとのことです。\nまた、本病の感染予防に関しては、マカク属のサルによる咬傷、擦過やサルに使用した注射針の針刺し、培養に使用したガラス器具等による外傷を防ぐことが重要となります。\n詳細はこちらをご覧ください。\n・https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/000130367_00001.html \n・https://www.mhlw.go.jp/content/10900000/000571901.pdf \n ・https://www.niid.go.jp/niid/ja/kansennohanashi/470-b-virus-info.html "
    elif len([s for s in ['運動','スペース','ケージ','空間','掃除','檻','かご','おり','カゴ','空く','空白','動'] if s in event.message.text]) >= 2:
       reply_message = "〈寝床や休息場所となるケージ〉\n● 犬:タテ(体長の2倍以上)×ヨコ(体長の1.5倍以上)×高さ(体高の2倍以上)\n● 猫:タテ(体長の2倍以上)×ヨコ(体長の1.5倍以上)×高さ(体高の3倍以上)、1つ以上の棚を設け2段以上の構造とする。\n● 複数飼養する場合:各個体に対する。上記の広さの合計面積と最も体高が高い個体に対する上記の高さを確保。\n〈運動スペース〉\n● 下記の一体型飼養等と同一以上の広さを有する面積を確保し、常時運動に利用可能な状態で維持管理する。"
    elif len([s for s in ['運動','床','面積','地面','表面積','体積','土地','設知','が床','壁面','天井','ゆか'] if s in event.message.text]) >= 2:
       reply_message = "犬:床面積(分離型ケージサイズの6倍以上)×高さ(体高の2倍以上)\n複数飼養する場合:床面積(分離型ケージサイズの3倍以上×頭数分)と最も体高が高い犬の体高の2倍以上を確保。※床面積は、同時に飼養する犬のうち最も体長が長い犬の床面積の6倍以上が確保されていること。\n● 猫:床面積(分離型ケージサイズの2倍以上)×高さ(体高の4倍以上)、2つ以上の棚を設け3段以上の構造とする。   複 数 飼 養 す る 場 合 : 床面積(分離型ケージサイズの面積以上×頭数分)と最も体高が高い猫の体高の4倍以上を確保。※床面積は、同時に飼養する猫のうち最も体長が長い猫の床面積の2倍以上が確保されていること。\n● 繁殖時:親子当たり上記の1頭分の面積を確保(親子以外の個体の同居は不可)。"
    elif len([s for s in ['第二種','業種','種類','業態','業','数種類','種','分野','職種','職業','形態','取扱い'] if s in event.message.text]) >= 2:
       reply_message = "第二種動物取扱の種類のその内容は以下の5つになります。譲渡：飼養施設を有し、非営利で動物の譲渡を行う等。保管：専用の飼養施設を有し、非営利で動物の預かりを行う等。貸出し：専用の飼養施設を有し、非営利で貸出しの公的な活動を行う等。訓練：専用の飼養施設を有し、非営利で盲導犬等の訓練など公的な活動を行う等。展示：専用の飼養施設を有し、非営利で公園展示等の活動を行う等。"
#譲渡・しつけ
    elif len([s for s in ['犬','猫','しつけ方','ネコ','しつける','飼い方','教え','子犬','愛犬','飼犬'] if s in event.message.text]) >= 2:
       reply_message = "犬・猫のしつけ方についてのご相談ですね。\nここでは、あなたに合った犬・猫に関する教育等のイベントをご紹介できます。\n紹介を希望される場合は、「イベントの紹介」と送信ください！"
    elif len([s for s in ['譲渡前講習会','受け','受講','講義','うけ','受ける','セミナー','講座','開講','講師','講習','行なっ'] if s in event.message.text]) >= 2:
       reply_message = "譲渡前講習会についてですね。講習会はオンラインで受講いただけます。オンライン受講の流れは以下の4ステップになります。\n\n1.以下のURLから、電子申請にて、受講の申し込みを行う。https://dshinsei.e-kanagawa.lg.jp/140007-u/profile/userLogin_initDisplay.action?nextURL=CqTLFdO4voZD9uOPm3Nmau3BB%2BFN7Gi4KMXGdBKterQfdrrJ0c3uG49wiM9ZpSVrEPgn8SiNxXCv%0D%0A1FXxyDAFxYzNnOoECHreFqLsJJO%2B9FMjbRATJd6Qs9iY1TDGt33ftT3gvrp1Ff0%3D%0D%0A \n\n2.自動返信メールに記載されているURLから、講習会の動画を視聴・受講する。\n\n3.ご覧いただいた動画のコメント欄に記載している電子申請URLから、譲渡前講習会受講証交付申請を行う。\n\n4.当所で確認後、後日受講証交付に係る返信メールが来たことを確認する。\n\n※注意点※・URLの公開等はご遠慮ください。\n・動画視聴にあたってのデータ通信料は受講者負担となりますので、視聴環境はwifi等の環境を推奨します。\n・動画の視聴をいただいたことの確認のために、感想欄等がありますので、漏れなく記入をお願いします。　講習会は来所しての受講もご利用いただけます。ご希望の際は個別対応となりますので、当所(0463-58-3411)までお電話ください。"
    elif len([s for s in ['譲渡','希望','引取り','譲り受ける','流れ','貸与','要望','数','について','引き取っ','引取','引き取る','引き取れる','引き取れ'] if s in event.message.text]) >= 2:
       reply_message = "犬・猫の譲渡には以下の三つの手順が必要になります。\n\n1.譲渡前講習会を受ける。\n2.個別面接を受ける\n3.譲り受ける。譲渡講習会の受講を希望する場合は、「譲渡講習会を受講したい」と送信ください。より詳細な情報についてはこちらをご覧ください。https://www.pref.kanagawa.jp/osirase/1594/awc/receive/about.html"
    elif len([s for s in ['犬','猫','動物','飼えない','引き取り','飼え','ペット','飼育','引き取っ','引き取れ','引き取れる','引き取る',] if s in event.message.text]) >= 2:
       reply_message = "動物は家族の一員として最期の時まで飼っていただくことが原則です。\nもし事情があって飼えなくなったら、まず、ご自身で新たな飼い主を探す努力をお願いします。噛み付くなど攻撃性がある場合は、訓練士によるしつけ・矯正を検討してください。\nどうしても新たな飼い主が見つからない場合や問題が解決しない場合は、飼い主自らの意思で今までかわいがってきた動物を殺すことになってしまう可能性があるという現実について、ご家族を含めて真剣に話し合ってください。\n引取りは、これらの事情を聞いた上での対応となります（有料）。"
    elif len([s for s in ['福祉','保健所','どうぶつ','愛護センター','センターとは','あいご','県'] if s in event.message.text]) >= 2:
       reply_message = "神奈川県動物愛護センターは、令和元年、「動物を処分するための施設」から「生かすための施設」へと機能を転換し、新たに開所されました。\n当施設は県民の動物愛護意識の高まりに伴い、各保健所で実施していた犬の捕獲抑留等の業務効率化のために生まれました。\n「人と動物の調和のとれた共生」の実現を目指して、動物が人間社会の中でよりよい関係を保つための事業を推進しています。\n神奈川県動物愛護センターのホームページはこちらです！ https://www.pref.kanagawa.jp/osirase/1594/awc/ "
    elif len([s for s in ['ありが','とう','さん','きゅ','サン','キュ','有','難う'] if s in event.message.text]) >= 2:
       reply_message = "どういたしまして！\n少しでもお役に立てたのなら嬉しいです！\nまた、御用があれば質問してください。"
    elif len([s for s in ['アイ','コ','あい','こ'] if s in event.message.text]) >= 2:
       reply_message = "私は神奈川県動物愛護センターのアイコです！精一杯質問に答えますのでよろしくお願いします！"
    elif len([s for s in ['お','は'] if s in event.message.text]) >= 2:
       reply_message = "おはようございます！何か質問はありますか？"
    elif len([s for s in ['こん','に'] if s in event.message.text]) >= 2:
       reply_message = "こんにちは！何か質問はありますか？"
    elif len([s for s in ['こん','ば'] if s in event.message.text]) >= 2:
       reply_message = "こんばんわ！何か質問はありますか？"

    else:
        reply_message = f"申し訳ございません。{event.message.text}については、読み込めませんでした。他の文章を入力してください。例えばこのように質問してみてください。\n\n・場所はどこにありますか\n・餌代はいくらかかりますか\n\n上記のように質問いただくと、回答できる場合があります。オペレーターによる対応も行っております。希望する場合は「オペレーターと会話」と送信ください。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))
 
if __name__ == "__main__":
    app.run()
