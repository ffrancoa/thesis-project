THESIS_FILE = main.typ
OUTPUT_FILE = thesis.pdf

all: $(OUTPUT_FILE)

$(OUTPUT_FILE): $(THESIS_FILE)
	typst compile $(THESIS_FILE) $(OUTPUT_FILE)

clean:
	rm -f $(OUTPUT_FILE)
