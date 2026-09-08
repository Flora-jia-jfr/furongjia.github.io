# Furong Jia's academic website

A personal academic website with a sticky top navigation, a wide reading column, a sticky profile on desktop, all publications, and separate experience, service, and CV pages. The design takes inspiration from Minimal Light; the layout, styles, and generator are written for this site. No Jekyll theme, frontend framework, or package installation is required.

Live website: https://flora-jia-jfr.github.io/furongjia.github.io/

## 更新内容

主要编辑 **`content/site.json`**，然后运行：

```sh
python3 scripts/build.py
python3 scripts/check.py
```

生成的 HTML 文件需要一起提交。GitHub Pages 直接发布 `main` 分支的根目录；合并到 `main` 后会自动更新，不需要改变 Pages 设置。

| 内容 | 编辑位置 |
| --- | --- |
| 姓名、邮箱、照片、CV 链接 | `profile` |
| 原有 bio 的三个段落 | `about`（保留原文、HTML 链接及加粗；不要自动改写） |
| 全部论文和预印本 | `publications` |
| 学历 | `education` |
| Research experience | `research_experience` |
| Teaching | `teaching` |
| Academic service | `service` |
| 荣誉 | `honors` |

### 添加论文

在 `publications` 数组加入一项：

```json
{
  "id": "unique-paper-name",
  "title": "Paper title",
  "authors": "First Author, Furong Jia, Last Author",
  "year": 2026,
  "venue": "Conference 2026",
  "links": [
    {"label": "Paper", "url": "https://example.org/paper"},
    {"label": "Code", "url": "https://github.com/example/repository"}
  ]
}
```

- `id` 必须唯一，用于论文链接锚点。
- 所有论文显示为一个连续列表，不显示年份分组或 Preprints 分组。未发表的论文可将 `venue` 写为 `arXiv`，也可留空。
- `year` 仅用于倒序排序；同一年内按数据文件的排列顺序显示。会议名称和年份按 `venue` 原文展示。
- 本人的名字自动加粗，不需要在作者字段手写 HTML。
- Paper、Code、Project、Slides 等入口统一使用 `links`，不需要独立 Projects 栏目。

### 更新照片与简历

照片位于 `figures/me.jpg`。CV 文件位于 `files/`，具体文件名由 `profile.cv` 指定。替换 PDF 后，如果文件名变化，也要同步更新这个字段。

### 调整排版

编辑 `assets/site.css`。桌面最大宽度在 `.site-layout` 中设为 `1200px`，左栏 `244px`，右栏使用余下空间。顶部固定显示导航和太阳／月亮外观图标；左栏仅显示照片和个人信息，使用 `position: sticky` 停在导航下方。整个文档正常滚动，没有两套嵌套滚动条。窄屏或过矮的窗口恢复自然流布局，以保证所有链接可达。

## 本地预览

在仓库根目录运行：

```sh
python3 -m http.server 8000
```

打开 http://localhost:8000 。网站内容预先生成为 HTML，禁用 JavaScript 时仍可阅读。JavaScript 仅用于本机保存的明暗外观偏好。

## 分支与发布

建议在自己的仓库中新建分支、预览并发起 PR，然后合并到 `main`：

```sh
git switch -c update/publications
# Edit content/site.json
python3 scripts/build.py
python3 scripts/check.py
git add content/site.json index.html publications.html experience.html service.html cv.html
git commit -m "Update website content"
git push -u origin update/publications
```

PR 的目标仓库应为 **`Flora-jia-jfr/furongjia.github.io`**，不是以前的模板仓库。当前设置为 Settings → Pages → Deploy from a branch → `main` → `/ (root)`。

如果需要从 GitHub 的 fork network 中独立出来，另参阅 [GitHub: Detaching a fork](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/detaching-a-fork)。这与网页重设计分开处理；离开 fork network 是不可逆操作，且 GitHub 文档提示可能丢失 issues、PR 等仓库元数据。单纯更新网页不需要执行此操作。

## 页面与源文件

```text
content/site.json    # 个人内容的单一来源
templates/base.html # 所有页面共用的布局
scripts/build.py    # 生成页面；只依赖 Python 标准库
scripts/check.py    # 检查本地链接、锚点、照片、论文完整性与顺序
assets/site.css     # 字体、宽度、留白、响应式布局
assets/site.js      # 明暗外观切换
index.html          # About + 全部论文 + 简短 Academic Service
publications.html   # 保留已有 URL 的完整论文专页
experience.html     # Research experience + Teaching + Honors
service.html        # Academic Service + Teaching
cv.html             # PDF 简历 + Education
```

以前的 `projects.html` 跳转到首页论文区，`blogs.html` 和 `photography.html` 跳转到首页。已有论文图、照片和 PDF 路径保留，旧模板源代码仍可在 Git 历史中找到。

## Design references

- [Minimal Light](https://github.com/yaoyao-liu/minimal-light): visual inspiration for the profile / reading-column composition.
- The previous website used the [Academic Homepage Template](https://github.com/Arvid-pku/Academic-Homepage-Template), with credit to Jon Barron and Xunjian Yin. This redesign preserves Furong Jia's existing academic content and assets.
