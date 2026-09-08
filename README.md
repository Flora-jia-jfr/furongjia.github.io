# Furong Jia’s academic homepage

Source for [Furong (Flora) Jia’s personal academic website](https://flora-jia-jfr.github.io/furongjia.github.io/).

The site presents my research interests, publications, academic service, research experience, and CV. It uses static HTML generated from a shared layout and a single content file, with no frontend framework or package installation required.

## Design and colors

The design uses a wide reading column, a portrait sidebar, serif headings, and a restrained **Duke-inspired custom blue palette**.

| Color | Light appearance | Dark appearance |
| --- | --- | --- |
| Headings, links, and icons | `#234F70` | `#AACDE8` |
| Page background | `#FFFFFF` | `#151C24` |
| Body text | `#303C48` | `#E2E8EF` |

These are custom colors. For comparison, the [official Duke palette](https://brand.duke.edu/colors/) defines Duke Navy Blue as `#012169` and Duke Royal Blue as `#00539B`.

## Updating the site

Edit `content/site.json`, then regenerate and check the pages:

```sh
python3 scripts/build.py
python3 scripts/check.py
```

Commit the content changes together with the generated HTML. GitHub Pages publishes the root of `main`.

For a local preview:

```sh
python3 -m http.server 8000
```

Open [localhost:8000](http://localhost:8000). See [maintenance notes](docs/maintenance.md) for updating publications, photos, the CV, and layout.

## Credits

- [Minimal Light](https://github.com/yaoyao-liu/minimal-light) inspired the profile and reading-column layout.
- Source Serif 4 is hosted locally under the [SIL Open Font License](assets/fonts/OFL.txt).
- Social logos are from [Font Awesome Free](https://fontawesome.com/license/free), with the [license included](assets/icons/LICENSE.txt).
- Historical template attribution is retained in the [maintenance notes](docs/maintenance.md#design-references).
