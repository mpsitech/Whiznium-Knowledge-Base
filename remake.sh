make clean

make html
for kb_dir in "$PWD"/KB*; do
	if [ -d "$kb_dir" ]; then
		kb_name=$(basename "$kb_dir")
		cp -r "$kb_dir" "$PWD/_build/html/"
	fi
done
touch _build/html/.nojekyll
