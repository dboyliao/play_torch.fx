run-debug:
	lldb -s .lldb-cmds $$(pyenv which python3) -- -m pdb test_custom_eval_frame.py

gh-page-worktree:
	@if [ ! -e worktree/gh-pages ]; then \
		mkdir -p worktree; \
		git worktree add \
		--checkout worktree/gh-pages gh-pages; \
	fi;

slides:
	@cd notebooks; \
	make

update-slides: gh-page-worktree slides
	@cp notebooks/intro_torchdynamo.slides.html worktree/gh-pages/index.html
	@cp -r notebooks/img worktree/gh-pages

COMMIT_MESSAGE?='update gh-page slides'
push-slides:
	@cd worktree/gh-pages; \
	git add -A; \
	git commit -m $(COMMIT_MESSAGE); \
	git push origin gh-pages;