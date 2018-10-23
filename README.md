# MOOCScraper
This Scrapy spider crawls [Class Central](https://www.class-central.com/subjects) and gathers key details on listed MOOCs. The collected information is then dumped into a local PostgreSQL database.
The project is based on an assignment I completed for a [Scrapy course](https://www.udemy.com/scrapy-tutorial-web-scraping-with-python/), which I extended to make use of other functionalities such as:
* Items and item loaders
* Custom input/output processors
* Database pipeline
* PostgreSQL and SQLAlchemy

## Dependencies
This spider was built with [Scrapy 1.5.0](https://scrapy.org/) for Python 3.6. The spider also uses python-dotenv and SQLAlchemy. For a full list of dependencies, please refer to the `requirements.txt` file.

## Setup
Please follow these instructions to set up the spider.

### Cloning the Project
1. Clone this repo
2. Create and activate a fresh virtual environment for this project
3. `cd` to the project root directory in your shell
4. Run `pip install -r requirements.txt` in your shell

### Database Setup
1. Create a new PostgreSQL database (refer to the [documentation](https://www.postgresql.org/docs/) for complete instructions)
2. Create a blank file named `.env` in the project root directory
3. Enter database connection and authentication details (from step 1) into the `.env` file as the following environment variables (make sure to specify the correct values that refer to your own db configuration):

```
DB_DRIVER_NAME=postgres
DB_HOST=localhost
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

## Usage
To run the spider:
1. Start the PostgreSQL server ([see here](https://www.postgresql.org/docs/9.1/static/server-start.html) for complete instructions)
2. Run `scrapy crawl class_central` in another shell (make sure to activate the appropriate virtual environment)

## Output
Each record includes the following fields (some records may not have values for all fields):
* `course`: the name of the course
* `subject`: which subject the course belongs
* `university`: which institution offers the course
* `provider`: the online platform where the course can be found
* `start_date`: the course start date
* `duration`: how long the course will take
* `link`: the course URL
* `date_scraped`: the date and time when the course page was scraped

## License
[MIT License](https://opensource.org/licenses/MIT)

## Contributing
Please feel free to contribute in whatever way you deem fit.