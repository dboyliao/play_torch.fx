SLIDES_THEME?=beige

intro-dynamo-slides: intro_torchdynamo.ipynb
	jupyter nbconvert --to slides $< --reveal-prefix=https://unpkg.com/reveal.js@5.1.0 --SlidesExporter.reveal_theme=${SLIDES_THEME}