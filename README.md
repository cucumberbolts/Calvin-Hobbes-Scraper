# Comic-Scraper
A single python file for downloading comics from gocomics.com.

## Usage
Run the comic_scraper.py file and pass the command line arguments specifying
the date (MM/DD/YYYY) and the comic with `--date` and `--comic` respectively.
Example:
```
python comic_scraper.py --date 09/07/2020 --comic "Calvin and Hobbes"
```

You can use "today" in place of the current date.

```
python comic_scraper.py --date today --comic "Calvin and Hobbes"
```

If no arguments were entered, then you will be prompted to enter them.
