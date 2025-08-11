/**
 * Created by Sobey on 2017/10/30.
 */
//APP用户
var app_token,cookie,user_token;
var u = navigator.userAgent;
var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/); //ios终端
function appUser(){
    cookie = getCookie("ysz_app_user");
    try{
         if (isiOS) {
                user_token  = localStorage.getItem("getLoginToken");
            } else {
                user_token = window.callNative.getLoginToken();
            }
		user_token = JSON.parse(user_token);
        app_token = user_token.token;
        if(app_token==undefined||app_token=="undefined"){
            app_token=cookie;
        }else{
			$(".header").hide();
			$(".footer").hide();
			$(".comment_more").hide();
			$(".article-app-tips").hide();
            delCookie("ysz_app_user");
            setCookie("ysz_app_user", app_token, 7 * 24 * 3600);
        }
        
        //$(".title").html(app_token);
    }catch(err){
        if (cookie){
            $(".header").hide();
            $(".footer").hide();
			$(".comment_more").hide();
            $(".article-app-tips").hide();
            app_token=cookie;
            //$(".title").html(app_token+"kkk");
        }else{
            //$(".header").show();
            $(".footer").show();
            $(".article-app-tips").show();
            //$(".title").html("hh");
        }
    }
}
//三个参数，一个是cookie的名字，一个是值，一个是过期时间单位秒
function setCookie(name, value, time) {

    var cookieStr = name + "=" + escape(value);

    if (time > 0) {

        var date = new Date();

        date.setTime(date.getTime() + time * 1000);

        cookieStr += ";expires=" + date.toGMTString();

    }

    document.cookie = cookieStr + ";path=/";

}
//取cookies函数
function getCookie(name) {

    var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));

    if (arr != null) return unescape(arr[2]);
    return null;

}
//删除cookie
function delCookie(name) {

    var exp = new Date();

    exp.setTime(exp.getTime() - 10000);

    var cval = getCookie(name);

    if (cval != null) document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();

}












