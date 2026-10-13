"""Build the static site and discover slides automatically. No dependencies."""
from pathlib import Path
from urllib.parse import quote
import json, shutil
ROOT = Path(__file__).resolve().parents[1]
COURSES = ('01-introduction', '02-parameter-estimation', '03-population', '04-searches', '05-electromagnetic-counterparts')
def build(output=None):
    output = Path(output) if output else ROOT / '_site'
    if output.exists(): shutil.rmtree(output)
    shutil.copytree(ROOT / 'site', output)
    manifest = {}
    for course in COURSES:
        manifest[course] = []
        folder = ROOT / 'slides' / course
        for source in sorted(folder.iterdir(), key=lambda p: p.name.casefold()):
            if not source.is_file() or source.is_symlink() or source.suffix.lower() not in {'.pdf', '.ppt', '.pptx'}: continue
            destination = output / 'slides' / course / source.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            manifest[course].append({'name':source.name,'size':source.stat().st_size,'url':'slides/'+course+'/'+quote(source.name,safe='')})
    (output / 'assets' / 'slides.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2),encoding='utf-8')
    (output / '.nojekyll').touch()
    print(f'Built {output}; {sum(map(len,manifest.values()))} slide files')
    return output
if __name__ == '__main__': build()
