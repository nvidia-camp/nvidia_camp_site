"""모든 페이지 공통으로 끼우는 것: 위쪽 메뉴, 라이트/다크 전환, 방문 통계."""
import html
import re

from .config import HERE, ICON_VIEW, SITE_NAME, web, web_script
from .data import image_data


# ── 내용 페이지 위쪽 메뉴 ────────────────────────────────────────────────
NAV_CSS = "<style>\n" + web("nav.css") + "</style>"
DOWNLOAD_MARK = "<!--download-->"  # copy_page가 'HTML 받기' 링크로 바꾼다
THEME_MARK = "<!--theme-->"        # 다크 모드가 있는 페이지면 테마 버튼으로, 없으면 빈 글자로 바꾼다


# ── 라이트/다크 전환 ─────────────────────────────────────────────────────
# 페이지마다 다크 CSS는 @media (prefers-color-scheme:dark) 안에 있다. 버튼을 누르면 그 media 조건을
# 항상 참/항상 거짓으로 바꿔 끼워 OS 설정과 관계없이 고른 쪽을 보여 준다. 고른 값은 localStorage에 둔다.
# OS 설정과 같은 쪽을 고르면 저장값을 지워 다시 OS 설정을 따른다.
# 본문 속 <style>(강의 목차 블록 등)도 첫 화면 전에 바꾸도록 파싱 중 추가되는 style을 지켜본다.
THEME_HEAD = web_script("theme.js") + "\n<style>\n" + web("theme.css") + "</style>"
THEME_BTN = ('<button class="theme-toggle" type="button" aria-label="화면 밝기 바꾸기" data-tip="화면 밝기 바꾸기">'
             '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
             '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4'
             'M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>')


# ── 맨 위로 버튼 (강의 요약 페이지) ──────────────────────────────────────
# 꺾쇠 아이콘 + 읽은 만큼 차는 원. 모양 web/totop.css, 동작 web/totop.js.
# 어두운 색(web/totop-dark.css)은 다크 모드가 있는 페이지에만 붙인다.
TOTOP_BTN = ('<button class="to-top" type="button" aria-label="맨 위로" title="맨 위로">'
             '<svg class="tt-ring" viewBox="0 0 44 44" aria-hidden="true"><circle class="tt-track" cx="22" cy="22" r="21"/>'
             '<circle class="tt-bar" cx="22" cy="22" r="21"/></svg>'
             '<svg class="tt-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><path d="m18 15-6-6-6 6"/></svg></button>')


def add_totop(text, dark):
    """</body> 바로 앞에 맨 위로 버튼·CSS·JS를 넣는다."""
    css = web("totop.css") + (web("totop-dark.css") if dark else "")
    block = f"<style>\n{css}</style>\n{TOTOP_BTN}\n{web_script('totop.js')}\n"
    text, n = re.subn(r"</body>", lambda m: block + "</body>", text, count=1, flags=re.I)
    return text if n else text + block


def add_copy(text):
    """<pre data-copy>가 있는 페이지면 </body> 앞에 복사 버튼 CSS·JS를 넣는다 (모양 web/copy.css, 동작 web/copy.js)."""
    if not re.search(r"<pre\b[^>]*\bdata-copy\b", text):
        return text
    block = f"<style>\n{web('copy.css')}</style>\n{web_script('copy.js')}\n"
    text, n = re.subn(r"</body>", lambda m: block + "</body>", text, count=1, flags=re.I)
    return text if n else text + block


def add_theme(text, nav, dark):
    """다크 모드가 있는 페이지에만 테마 스크립트(</head> 앞)와 버튼(메뉴 오른쪽 끝)을 넣는다."""
    if not dark:
        return text, nav.replace(THEME_MARK, "")
    nav = nav.replace(THEME_MARK, THEME_BTN)
    text, n = re.subn(r"</head>", lambda m: THEME_HEAD + "\n</head>", text, count=1, flags=re.I)
    return text, (nav if n else THEME_HEAD + nav)


def nav_html(depth, crumbs, here=None, prev=None, next_=None, lecture=None, view=None, on_lecture=False, colab=None):
    """crumbs: [(이름, 루트 기준 경로)], here: 현재 위치 글자, prev/next_: (이름, 경로)
    on_lecture: 지금 사이트의 강의 HTML 화면이다 (Slack은 로고만)"""
    up = "../" * depth
    left = [f'<a href="{up or "./"}">← {SITE_NAME}</a>']
    left += [f'<a href="{up}{path}">{html.escape(name)}</a>' for name, path in crumbs]
    if here:
        left.append(f'<span class="cn-here">{html.escape(here)}</span>')
    right = [DOWNLOAD_MARK]
    if view:
        right.append(f'<a class="cn-ico" href="{html.escape(view)}" data-tip="강의 자료 보기" aria-label="강의 자료 보기">{ICON_VIEW}</a>')
    if lecture:   # 사이트에 강의 HTML이 있으면 Slack은 로고만, 없으면 Slack이 곧 강의 자료
        tip = "Slack 강의 자료 게시물 (새 탭)" if view or on_lecture else "강의 자료 · Slack 게시물 (새 탭)"
        right.append(f'<a class="cn-ico cn-slack" href="{html.escape(lecture)}" target="_blank" rel="noopener" data-tip="{tip}" aria-label="{tip}">'
                     f'<img src="{image_data(HERE / "assets" / "logos" / "slack-white.svg")}" alt="" width="16" height="16"></a>')
    if colab:
        right.append(f'<a class="cn-ico cn-colab" href="{html.escape(colab)}" target="_blank" rel="noopener" data-tip="Colab 실습 폴더 · Google Drive (새 탭)" '
                     f'aria-label="Colab 실습 폴더 (Google Drive, 새 탭)"><img src="{image_data(HERE / "assets" / "logos" / "colab-white.png")}" alt="" width="27" height="16"></a>')
    if prev:
        right.append(f'<a href="{up}{prev[1]}">‹ {html.escape(prev[0])}</a>')
    if next_:
        right.append(f'<a href="{up}{next_[1]}">{html.escape(next_[0])} ›</a>')
    side = f'<span class="cn-right">{"".join(right)}</span>{THEME_MARK}'   # 테마 버튼은 맨 끝 (좁은 화면에서 오른쪽에 고정)
    return f'{NAV_CSS}<nav class="cn-nav" aria-label="사이트 메뉴">{"".join(left)}{side}</nav>'


# 방문 통계: 모든 사이트 화면에 넣는다 (download.html 원본·강의 view.html에는 넣지 않는다)
# - Vercel Web Analytics (Vercel 프로젝트에서 Analytics를 켜 둬야 동작)
# - Google Analytics 4 (web/analytics.js): 실제 사이트 주소에서만 보낸다. 미리보기·로컬 확인은 통계에 섞이지 않는다.
#   주소 끝에 ?ga_debug=1 을 붙이면 GA 관리 > DebugView에서 이벤트를 바로 볼 수 있다.
#   페이지 공통 값(set): content_group(과목 키·home·setup·cheatsheet), page_type, day_label(메뉴의 DayNN)
#   이벤트: section_view(h2 단락이 화면에 들어옴, 페이지당 1회) · toc_open/details_open(접힌 상자 펼침)
#           site_click(모든 링크, link_type으로 구분) · theme_toggle · slide_view/lecture_progress(강의 화면)
GA_SCRIPT = web_script("analytics.js")
ANALYTICS = ('<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script>\n'
             '<script defer src="/_vercel/insights/script.js"></script>\n' + GA_SCRIPT)
