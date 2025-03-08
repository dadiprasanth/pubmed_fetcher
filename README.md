# PubMed Fetcher

PubMed Fetcher is a tool designed to help you retrieve and manage scientific articles from PubMed. This project aims to simplify the process of fetching and organizing research papers for your academic and professional needs.

## Features

- Fetch articles from PubMed using various search criteria
- Save articles in different formats (e.g., JSON, XML)
- Organize and manage your fetched articles
- Command-line interface for easy usage

## Installation

To install PubMed Fetcher, clone the repository and install the required dependencies:
step1 install poetry in your machine
``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
git https://github.com/dadiprasanth/pubmed_fetcher.git
cd pubmed_fetcher
poetry install
```

## Usage

To fetch articles from PubMed, use the following command:

```bash
get-papers-list "your--search-query" -f filename.csv

```

You can specify additional options such as the number of articles to fetch and the output format. For more details, use the `--help` flag:

```bash
get-papers-list --help
get-papers-list -h

```

## Contributing

We welcome contributions to PubMed Fetcher! If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at your.email@example.com.
