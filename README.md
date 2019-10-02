# Automatic decoration dataset

### Summary
Scraping top N websites on the Alexa ranking, downloading all images, filtering based on if the associated alt text is provided, but empty. If an alt attribute is provided but it's empty it means that it's mostly a decoration and is non-relevant to get the actual context of the website.

### Running
`python3 -m bin.build_decoration_dataset TOP_N OUT_DIRECTORY_PATH N_PROCESSES`

### Relevant papers
#### Creating datasets based on filtering large amounts of websites
* Conceptual Captions: A New Dataset and Challenge for Image Captioning

### Author
Oliver Edholm, 17 years old