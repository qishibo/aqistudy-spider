
 # Spider Of [aqistudy.cn]
 
 Visible charts in [https://qii404.me/aqistudy-spider/views/](https://qii404.me/aqistudy-spider/views/)

 ## Run:

 ```bash
// install node dependencies
npm install

// begin to crawl
scrapy crawl Pm25
 ```

## Node Parser

```
// crawl city's month data
node js-parser.js city month
```

## Tips:

You need to rewrite js params because the param in encrypt process is dynamic.
Catch from `https://www.aqistudy.cn/historydata/resource/js/encrypt_xxxx.min.js`

```javascript
const askCqjmcofkq = "ajNdtudubESiBmHr"; // need to be rewrite
const asibfJCC9wdl = "btNGSsEz7b0ibtWn"; // need to be rewrite
const ackBc07Yvwuj = "dQdwwRizO8YmD6gj"; // need to be rewrite
const aciGWpaar6yP = "fH6bGsU03RyYOHLL"; // need to be rewrite
const dskuv3VVb4Cu = "hTqf4BKstzxlIzIX"; // need to be rewrite
const dsi3eHGiqSTK = "xVNPGldlVpN8VtiP"; // need to be rewrite
const dckYewUZNGAG = "oEvQiT2YIPAviyOw"; // need to be rewrite
const dci6nhjGNsRa = "paPcaWF3WmORwUGK"; // need to be rewrite
const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

return function (method, obj) {
    var appId = '5a68158db26b30c19d53135e18ac1579'; // need to be rewrite
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    var param = {
        appId: appId,
        method: method,
        timestamp: timestamp,
        clienttype: clienttype,
        object: obj,
        secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = BASE64.encrypt(JSON.stringify(param));
    return param
}

$.ajax({
    url: 'https://www.aqistudy.cn/historydata/api/historyapi.php',
    data: {
        'hZj3cb0mx': param  // need to be rewrite
    },
```
