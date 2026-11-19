(function(){
var ID='G-9743VJ73E0';if(location.hostname!=='nvidiasesac.vercel.app')return;
var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+ID;document.head.appendChild(s);
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}window.gtag=gtag;gtag('js',new Date());
var d=document,dbg=/[?&]ga_debug=1/.test(location.search),PK='ga-pending-click';
function cut(t){return (t||'').replace(/\s+/g,' ').trim().slice(0,100)}
function ev(n,p){p=p||{};if(dbg)p.debug_mode=true;gtag('event',n,p)}
function init(){
  var seg=location.pathname.split('/').filter(Boolean),top=seg[0]||'home',type;
  if(!seg.length)type='home';else if(top==='setup')type='guide';else if(top==='cheatsheet')type='cheatsheet';
  else if(seg.length===1)type='subject';else if(/^\d{8}/.test(seg[1]))type=seg[2]==='lecture'?'lecture':seg[2]?'day_sub':'day';else type='other';
  var nav=d.querySelector('.cn-nav'),m=nav&&nav.textContent.match(/Day\d+(?:-\d+)?/);
  gtag('set',{content_group:top,page_type:type,day_label:m?m[0]:'(none)'});
  gtag('config',ID,dbg?{debug_mode:true}:{});
  try{var pend=sessionStorage.getItem(PK);if(pend){sessionStorage.removeItem(PK);ev('site_click',JSON.parse(pend))}}catch(x){}
  // 단락: h2가 화면 위쪽 60%까지 올라오면 한 번 (빠르게 스크롤해 지나친 단락도 세도록 위쪽 경계는 열어 둔다)
  if('IntersectionObserver' in window){
    var hs=[].slice.call(d.querySelectorAll('h2')).filter(function(h){return !h.closest('.cn-nav')});
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;io.unobserve(e.target);
      ev('section_view',{section_id:e.target.id||'(none)',section_title:cut(e.target.textContent),section_index:hs.indexOf(e.target)+1})})},{rootMargin:'100000px 0px -40% 0px'});
    hs.forEach(function(h){io.observe(h)});
  }
  // 접힌 상자: 강의 목차(lt-box)와 그 밖의 details
  d.addEventListener('toggle',function(e){var t=e.target;if(t.tagName!=='DETAILS'||!t.open)return;
    var sm=t.querySelector('summary');ev(t.classList.contains('lt-box')?'toc_open':'details_open',{details_label:cut(sm&&(sm.innerText||sm.textContent))})},true);
  // 링크
  d.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('.theme-toggle');
    if(b){setTimeout(function(){ev('theme_toggle',{theme:d.documentElement.getAttribute('data-theme')||''})},0);return}
    var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;
    var u=a.href,h=a.getAttribute('href'),ext=a.host&&a.host!==location.host,k;
    if(a.classList.contains('cn-colab')||/colab\.research|drive\.google/.test(u))k='colab';
    else if(a.classList.contains('cn-dl')||a.hasAttribute('download'))k='html_download';
    else if(a.classList.contains('cn-slack')||/slack\.com/.test(u))k='slack';
    else if(/swexpertacademy/.test(u))k='swea';else if(/programmers\.co\.kr/.test(u))k='programmers';
    else if(/\.pdf(\?|#|$)/i.test(u))k='pdf';else if(/(^|\/)lecture\/?$/.test(h))k='lecture_view';
    else if(h.charAt(0)==='#')k='anchor';else k=ext?'outbound':'internal';
    var p={link_type:k,link_text:cut(a.getAttribute('aria-label')||a.textContent),link_url:u,link_area:a.closest('.cn-nav')?'nav':'body',link_from:location.pathname};
    // 같은 탭에서 사이트 안 다른 페이지로 가면 떠나는 순간 이벤트가 사라질 수 있어 다음 페이지에서 보낸다
    if(!ext&&k!=='anchor'&&k!=='html_download'&&a.target!=='_blank'&&!e.defaultPrevented&&!e.ctrlKey&&!e.metaKey&&!e.shiftKey){
      try{sessionStorage.setItem(PK,JSON.stringify(p));return}catch(x){}}
    ev('site_click',p)},true);
  // 강의 화면: 슬라이드는 iframe 주소의 #id로 바뀐다(replaceState라 이벤트가 없어 1초마다 읽는다)
  var f=d.querySelector('iframe.lecture-frame');
  if(f){var last='',seen={},n=0,sent=false;
    setInterval(function(){var id='';try{id=f.contentWindow.location.hash.slice(1)}catch(x){return}
      if(!id||id===last)return;last=id;if(!seen[id]){seen[id]=1;n++}ev('slide_view',{slide_id:id,slides_seen:n})},1000);
    d.addEventListener('visibilitychange',function(){if(d.visibilityState==='hidden'&&n&&!sent){sent=true;ev('lecture_progress',{slides_seen:n,last_slide:last})}});
  }
}
d.readyState==='loading'?d.addEventListener('DOMContentLoaded',init):init();
})();
