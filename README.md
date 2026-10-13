# Gravitational Wave Group, PMO, CAS

Group website for Purple Mountain Observatory, Chinese Academy of Sciences.

## Publish

The source lives in `pmo-gwaves/pmo-gwaves.github.io`. In repository **Settings → Pages**, choose **GitHub Actions** as the publishing source. Push to `main` or run **Publish academic website** under Actions. The workflow builds and publishes `https://pmo-gwaves.github.io`.

## Upload lecture slides

Open the site's **workshop → 上传课件** link, choose a course, and upload PPT, PPTX or PDF files to GitHub. Commit to main; the build automatically updates the corresponding downloads. Multiple files per lecture and Chinese filenames are supported. Re-upload the same filename to replace it. Browser uploads support up to 25 MiB per file. Slides are public; only repository writers can upload.

## Edit

- `site/index.html`: group introduction, research, members and workshop link
- `site/workshop/index.html`: workshop schedule
- `site/assets/style.css`: typography and layout
- `slides/`: workshop files grouped by lecture

## Preview

```sh
python3 scripts/build.py
python3 -m http.server 8080 --directory _site --bind 127.0.0.1
```

The build requires only Python's standard library. Generated `_site/` is ignored.
