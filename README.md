# Python Scrapy Bookscraper

The Python Scrapy Bookscraper is a web scraping playbook adopted from [The Python Scrapy Playbook](https://thepythonscrapyplaybook.com/).

## Getting Started

Get started with the `Python Scrapy` project by following the steps below:

1. Install python virtual environment and activate.
2. Install required python modules for this project.
3. Create/View/Run Python Scrapy Spider.

### Step 1 - Install Python Virtual Environment and Activate

**1.1 Setup Python Virtual Environment On MacOS**

Run the following commands in the `project_folder`:

```bash
$ cd /project_folder
$ python3 -m venv venv
```

Activate the virtual environment so that any new pip install commands will install into the new `venv` folder:

```bash
$ source venv/bin/activate
```

**1.2 Setup Python Virtual Environment On Windows**

Install `virtualenv` if you haven't done so already.

```bash
pip install virtualenv
```

Run the following commands in the `project_folder`:

```bash
cd \project_folder
virtualenv venv
```

Activate the virtual environment so that any new pip install commands will install into the new `venv` folder:

```bash
source venv\Scripts\activate
```

**1.3 Setup Python Virtual Environment On Linux**

Install `python3-venv` if you haven't done so already.

```bash
$ sudo apt install -y python3-venv
```

Run the following commands in the `project_folder`:

```bash
$ cd /project_folder
$ python3 -m venv venv
```

Activate the virtual environment so that any new pip install commands will install into the new `venv` folder:

```bash
$ source venv/bin/activate
```

### Step 2 - Install Required Python Modules

To install the required modules for this python project run the following command:

```bash
pip install -r requirements.txt
```

### Step 3 - Create/View/Run Python Scrapy Spider

Once the required python modules are installed you should be able to create/view/run the Python Scrapy Spider with the below commands (from within the project folder, inside the spiders sub-directory).

* Create the project spiders:

```bash
cd bookscraper/spiders
scrapy genspider bookspider books.toscrape.com
```

* View the project spiders:

```bash
scrapy list
```

* Run the project spider:

```bash
scrapy crawl books
```



## Helpful Dubugging

If you have issues running the `pip install -r requirements.txt` command this can be due to some things not being up to date on your computer.

Running the following command may solve some of these issues:

```bash
pip install --upgrade pip
```

The following error: `NotADirectoryError: [Errno 20] Not a directory: 'pkg-config'` might be solvable by running the following command:

```bash
export PKG_CONFIG=/path/to/pkg-config
```
