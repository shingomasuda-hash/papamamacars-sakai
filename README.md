# PAPAMAMA CAR'S ららぽーと堺店｜試乗体験イベント LP

承認済み完成デザイン（JPG 585×11817px）をそのまま縦長LPとして公開する静的サイト。

- `public/index.html` … LP本体（GTM-KPB2C8K、LINE予約CTA×3、dataLayer計測）
- `public/images/lp-sakai.jpg` … 完成デザイン画像（Drive: `1uJEarhffBWRpE2AUlZn7EGehtHhcsSzL`）
- `tools/measure_cta.py` … 画像内のオレンジ色予約ボタンを検出し%座標を index.html に反映
- `vercel.json` … Vercel 静的配信設定（出力ディレクトリ `public`）

## クリック計測（dataLayer）

```js
{ event: 'line_reservation_click', store_name: 'sakai',
  cta_position: 'first_view' | 'middle' | 'bottom',
  destination_url: 'https://s.lmes.jp/landing-qr/2007227107-GgA3P6zw?uLand=Snwk74' }
```
