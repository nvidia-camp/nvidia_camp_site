(function(){
var K='site-theme',d=document,root=d.documentElement,mq=matchMedia('(prefers-color-scheme: dark)'),
RX=/\(\s*prefers-color-scheme\s*:\s*dark\s*\)/i,seen=[],rules=[],mem='';
function get(){try{var v=localStorage.getItem(K);return v==='dark'||v==='light'?v:''}catch(e){return mem}}
function put(v){mem=v;try{v?localStorage.setItem(K,v):localStorage.removeItem(K)}catch(e){}}
function scan(list){for(var i=0;i<list.length;i++){var r=list[i];
  if(r.media&&RX.test(r.media.mediaText))rules.push([r,r.media.mediaText]);if(r.cssRules)scan(r.cssRules)}}
function apply(){
  var ss=d.styleSheets;for(var i=0;i<ss.length;i++){var s=ss[i];if(seen.indexOf(s)<0){seen.push(s);try{scan(s.cssRules)}catch(e){}}}
  var f=get(),m=f||(mq.matches?'dark':'light');
  for(var j=0;j<rules.length;j++){var p=rules[j];
    p[0].media.mediaText=f?p[1].replace(RX,f==='dark'?'(min-width:0px)':'(max-width:0px) and (min-width:1px)'):p[1]}
  root.setAttribute('data-theme',m);root.style.colorScheme=f;
  var b=d.querySelectorAll('.theme-toggle'),t=m==='dark'?'밝은 화면으로 보기':'어두운 화면으로 보기';
  for(var k=0;k<b.length;k++){b[k].setAttribute('aria-label',t);b[k].setAttribute('data-tip',t)}}
d.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.theme-toggle');if(!b)return;
  var m=root.getAttribute('data-theme')==='dark'?'light':'dark';put(m===(mq.matches?'dark':'light')?'':m);apply()});
mq.addEventListener?mq.addEventListener('change',apply):mq.addListener(apply);
apply();
var mo=window.MutationObserver&&new MutationObserver(function(l){for(var i=0;i<l.length;i++)for(var j=0;j<l[i].addedNodes.length;j++){
  var n=l[i].addedNodes[j].nodeName;if(n==='STYLE'||n==='LINK'){apply();return}}});
if(mo)mo.observe(root,{childList:true,subtree:true});
d.addEventListener('DOMContentLoaded',function(){if(mo)mo.disconnect();apply()});
})();
