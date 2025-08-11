jQuery(document).ready(function($) {
    var readerNews;
    readerNews = {
        playStatus: "false",
        menImg: ["http://static.scms.sztv.com.cn/ysz/public_2019/img/menimg0.png",
            "http://static.scms.sztv.com.cn/ysz/public_2019/img/menimg1.gif"], //第二个gif代表动画效果
        girlImg: ["http://static.scms.sztv.com.cn/ysz/public_2019/img/womenimg0.png",
           "http://static.scms.sztv.com.cn/ysz/public_2019/img/womenimg1.gif"],
        textArry: [],
        length: 0,
        playObj: null,
        hasInit: !1,
        curParagraph: 0,
        contentClassName:".ysz_read_content",
        loadPage: 0,
        replay: 0,
        lastLoadTime: 0,
        bigPer: 0,
        ifChange: 0,
        formTTS: function (e) {
            var t = {
                    tex: encodeURI(e),
                    cuid: "ysz",
                    cod: 2,
                    lan: "zh",
                    ctp: 1,
                    pdt: 301,
                    spd: 5,
                    per: readerNews.bigPer,
                    vol: 5,
                    pit: 5
                },
                n = [];
            for (name in t) n.push(name + "=" + t[name]);
            return "http://tts.baidu.com/text2audio?" + n.join("&")
        },
        nextAudio: function () {

            var e = this.formTTS(this.textArry[this.curParagraph + 1]);
            $("html").append('<audio id="nextAudio" style="display:none" controls="" preload="load"><source src="' + e + '" type="audio/mp3"></audio>');

        },
        end: function (e) {

            var men_img = $(".men_speak");
            var girl_img = $(".women_speak");
            $(".men_speak").attr("_state", "0"),
                $(".women_speak").attr("_state", "0"),
                girl_img.attr("src", readerNews.girlImg[0]),
                men_img.attr("src", readerNews.menImg[0]);
        },
        decompose: function (e) {
            for (var t = Math.ceil(e.length / 500), n = [], i = 0; i < t; ++i) {
                var r = 500 * i;
                n.push(e.substr(r, 500))
            }
            return n
        },
        initData: function () {
            var e = this;
            e.textArry = [];
            $(".ysz_read_content p:not('.imagenote,.zwf,.afterVideo')").each(function (n, i) {
                 if($(this).css("opacity")==0 ||
                     $(this).css("display")=='none'){
                     // return true;
                 }else{
                     var r = $(this).text();
                     r = r.replace(/(^\s*)|(\s*$)|(▼)/g, ""),
                     r && (r.length > 500 ? e.textArry = e.textArry.concat(e.decompose(r)) : e.textArry.push(r))
                 }
             }), 
             e.length = e.textArry.length
            // var obj2 = $.extend(true, {}, $(".ysz_read_content"));
            // obj2.find("p.imagenote,p.zwf,:hidden,p.afterVideo").remove();
            // var  rText1=  obj2.text();
            // var r=  rText1.replace(/[\r\n]/g,"。").
            // replace(/[ ]/g,"").
           // replace(/(^\s*)|(\s*$)|(▼)/g, "");
            // r && (r.length > 500 ? e.textArry = e.textArry.concat(e.decompose(r)) : e.textArry.push(r)),
            // e.length = e.textArry.length
        },
        initParagraph: function () {
            var e = this;
            e.curParagraph = 0
        },
        initAll: function () {
            this.initData();
            this.initParagraph();
        },
        play: function () {
            // console.log("开始播放");
            // if (this.loadPage == 1) {console.log("stop play");return;}
            this.playObj.play(),
                this.playStatus = "playing",
                $(".listen_news").addClass("playing")

        },
        pause: function () {
            this.playObj.pause(),
                this.playStatus = "pause",
                $(".listen_news").removeClass("playing")
        },
        init: function () {
            if (this.loadPage == 1) {
                this.textArry = [];
                this.initData();
                this.setUnLoad();
            }
            this.nextAudio();
            if (this.playObj) "playing" == this.playStatus ? this.pause() : "pause" == this.playStatus ? (this.play(), console.log("继续.loadPage=" + this.loadPage)) : "end" == this.playStatus && (this.curParagraph = -1, this.changeMedium(), this.play());
            else {
                if (this.initData(), 0 == this.length) return !1;
                // console.log("第一步 开始.loadPage="+this.loadPage+"  "+this.textArry[this.curParagraph]);
                var e = this.formTTS(this.textArry[this.curParagraph]);
                $("html").append('<audio id="reader" style="display:none" controls="" ><source src="' + e + '" type="audio/mp3"></audio>'),
                    this.playObj = document.getElementById("reader"),
                    this.intEvent(),
                    this.play();
            }
        },
        destory: function () {
            this.pause()
        },
        intEvent: function () {
            var e = this;
            console.log("intEvent.loadPage=" + e.loadPage);
            var i = 0;
            this.playObj.addEventListener("ended",
                function (n) {
                    i++;
                    return e.curParagraph >= e.length - 1 ? (e.playStatus = "end", readerNews.end()) : (e.changeMedium(), e.play()),
                        !1
                },
                !1);

            this.playObj.addEventListener("play",
                function (n) {
                    e.nextAudio();
                },
                !1);
        },
        changeMedium: function () {
            ++readerNews.curParagraph,
                readerNews.playObj.src = readerNews.formTTS(readerNews.textArry[readerNews.curParagraph]);
        },
        setLoad: function () {
            this.loadPage = 1;
            this.replay = 1;
        },
        setUnLoad: function () {
            this.loadPage = 0;

        },
        readerNewsInit:function(){
            var yyldContentHtml='<span>人工智能朗读：</span><img  _state="0" class="women_speak" href="javascript:;"><img class="men_speak" _state="0" href="javascript:;" >';
            $(".yyld-btn").html(yyldContentHtml);
            $(".yyld-btn").css({ 'padding':"0 18px",'height':"35px", 'line-height':"35px", 'margin-bottom':'20px', 'overflow':'hidden', zoom:1})
            $(".yyld-btn span").css({ "margin-top":"2px","font-size":"16px","display":"block", "float":"left","color": "#999999",})
            $(".yyld-btn img").css({ "width":"31px", "height":"20px","float":"left", "margin":"9px 10px 0px 0px","cursor":"pointer",})
            $(".yyld-btn .men_speak").attr("src",readerNews.menImg[0])
            $(".yyld-btn .women_speak").attr("src",readerNews.girlImg[0])
        }
    };

    readerNews.readerNewsInit();
    $(".artical-con").bind("DOMNodeInserted",function(){
        readerNews.setLoad();
        readerNews.initData();
    });

    $(".men_speak").click(function(){

        //如果正在播放，且为男声
        var men_img = $(".men_speak");
        var girl_img = $(".women_speak");
        var state = $(this).attr("_state");

        state == 0 ? ($(".men_speak").attr("_state","1"), $(".women_speak").attr("_state","0"), men_img.attr("src",readerNews.menImg[1]),girl_img.attr("src",readerNews.girlImg[0]) ):
            ($(".men_speak").attr("_state","0"),  men_img.attr("src",readerNews.menImg[0]));
        readerNews.playStatus == "playing" || readerNews.playStatus == "pause" ? (readerNews.bigPer == 1 ? readerNews.init() : (readerNews.bigPer = 1,readerNews.playStatus='end',readerNews.ifChange = 9999,console.log("更换男声"),readerNews.init())):(readerNews.bigPer=1, readerNews.init());


    });

    $(".women_speak").click(function(){
        var men_img = $(".men_speak");
        var girl_img = $(".women_speak");
        var state = $(this).attr("_state");

        state == 0 ? ($(".men_speak").attr("_state","0"), $(".women_speak").attr("_state","1"), girl_img.attr("src",readerNews.girlImg[1]), men_img.attr("src",readerNews.menImg[0])) :
            ($(".women_speak").attr("_state","0"), girl_img.attr("src",readerNews.girlImg[0]));

        readerNews.playStatus == "playing" || readerNews.playStatus == "pause" ? (readerNews.bigPer == 0 ? readerNews.init() : (readerNews.bigPer = 0,readerNews.playStatus='end',readerNews.ifChange = 9999,console.log("更换女声"),readerNews.init())):(readerNews.bigPer=0, readerNews.init());

    });
});
