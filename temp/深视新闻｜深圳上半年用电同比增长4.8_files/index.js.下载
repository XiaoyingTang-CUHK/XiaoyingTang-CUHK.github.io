// 图片新闻
$(function(){
    var num=$('#slider').find('li').size();
    $('.bcount').text(num);
})
var tt=new TouchSlider({id:'slider','auto':'-1',fx:'ease-out',direction:'left',speed:600,timeout:5000,'before':function(index){

    var es=document.getElementById('slider').getElementsByTagName('li');

    var it=$(es[index]).index()+1;

    $('.bi').text(it);

    var tx=$(es[index]).find('p').text();

    $('.title').text(tx);

}});

function loadScript(){
    var script = document.createElement("script");
    script.type = "text/javascript";
    if (script["readyState"]){  // 仅限IE
       script["onreadystatechange"] = function(){
           if (script["readyState"] == "loaded" || script['readyState'] == "complete"){
                    script["onreadystatechange"] = null;
           }
       };
    } else {  // 其他浏览器
       script.onload = function(){
           console.log("js 加载完成,");
           new VConsole();
       };
    }
        // 设置脚本URL开始加载
   script.src = "https://www.sztv.com.cn/huodong/sj/common/js/vconsole.min.js";
   document.getElementsByTagName("head")[0].appendChild(script);
}
function getQueryValueBydev(name){
	let search = window.location.href.split('?')[1]
    if (!search) {
        return ''
    }
    search = search.split('#')[0];
    if (!search) {
        return ''
    }
    let reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)')
    let r = search.match(reg)
    if (r != null) {
        return `${r[2]}`
    }
    return ''
}
if(getQueryValueBydev("dev") === "cs"){
    loadScript();
}


// 微直播
$('#tab1').click(function(){
	console.log(1);
})
var $bd = $(".live-body .bd");
var $li=$('#livetab li a');
var currIndex = 0;
$(function () {
    $("#livetab li").click(function () {
        $bd[currIndex].style.display="none";
        $li[currIndex].setAttribute('class','');
        var index = $(this).index();
        $bd[index].style.display="block";
        $li[index].setAttribute('class','selected');
        currIndex=index;
    })
})
    const noChangeArticleIds = ["80349755","80243240","80159106","79995406"];
    function getAsideTitle(){
        const element = document.querySelector('p.aside-title');
        const ar = $("#article").val();
        console.log("article:",ar);
        if (element && !noChangeArticleIds.includes(ar)) {
          element.textContent = '第一现场';
        }
        const ele = document.querySelector('a.open');
        if(ele && !noChangeArticleIds.includes(ar)){
            ele.style.backgroundColor = "#FF4692";
        }
        const imgEle = document.querySelectorAll('aside > img');
        if(imgEle.length && noChangeArticleIds.includes(ar)){
            imgEle[0].setAttribute('src', 'https://www.sztv.com.cn/ysz/detail_2023/img/old_logo.jpg');
        }
    }
    getAsideTitle();

for(var i = 0; i< $(".article-content img").length; i++ ) {
    var src=$(".article-content img").eq(i).attr('src');
    $(".article-content img").eq(i).attr({'data-echo':src,"src":src,"data-preview-src":"","data-preview-group":"1"});
}
Echo.init({
    offset: 0,
    throttle: 0
});
// mui.init({
    // gestureConfig:{
	    // tap: true, //默认为true
	    // doubletap: false, //默认为false
	    // longtap: true, //默认为false
	    // swipe: true, //默认为true
	    // drag: false, //默认为true
	    // hold:false,//默认为false，不监听
	    // release:false//默认为false，不监听
    // }
// });
//微信判断
function isWX(){
    var ua = window.navigator.userAgent.toLowerCase();
    if(ua.match(/MicroMessenger/i) == 'micromessenger'){
        return true;
    }else{
        return false;
    }
}
        function imginfo(){
   var imglis = [];
   var imgObj = $("#editWrap  img");//img对象
   for(var i=0; i<imgObj.length; i++){
        if(imgObj.eq(i).attr('src')&&imgObj.eq(i).attr('class')!="expand-cover"){
            imglis.push(''+imgObj.eq(i).attr('src'))
         }      
         console.log(''+imgObj.eq(i).attr('src'))
         imgObj.eq(i).click(function(){
         console.log($(this).attr('src'))
         var Imgurl = ''+$(this).attr('src');
         WeixinJSBridge.invoke("imagePreview",{
           "urls":imglis,
           "current":Imgurl
         });
   });
   }

 }
 if(isWX()){
    imginfo();
 }else{
   //图片放大预览
   mui.previewImage();
}


   var imgObj1 = $("#editWrap a");//img对象
   for(var i=0; i<imgObj1.length; i++){
        if(imgObj1.eq(i).attr('alt')=="点击查看大图"){
            imgObj1.eq(i).attr('href','').attr("target",'');
         }      
   }
