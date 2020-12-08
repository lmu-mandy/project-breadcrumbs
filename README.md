![contributors-shield]
![license-shield]

<!-- PROJECT TITLE -->
<br />
<p align="center">
  <h3 align="center">Fairy Tale Text Generator</h3>

  <p align="center">
    By Project Breadcrumbs
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The goal of the project is to create a text generation model that will learn from existing fairy tales and auto-generate new and plausible fairy tale texts.

### Data and Models

* GPT-2
* Data sets used:
    * [Hans Christian Andersen Tales](http://www.gutenberg.org/ebooks/27200)
    * [Perrault Fairy Tales](http://www.gutenberg.org/files/29021/29021-h/29021-h.htm)
    * [Grimms' Fairy Tales](https://www.gutenberg.org/files/2591/2591-h/2591-h.htm)
    * [The Blue Fairy Book](http://www.gutenberg.org/files/503/503-h/503-h.htm) (Mixed Authors)
    * [Japanese Fairy Tales](http://www.gutenberg.org/files/4018/4018-h/4018-h.htm)

<!-- INSTALLATION -->
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lmu-mandy/project-breadcrumbs.git
   ```
2. Navigate to either `author_specific_fine_tuned_model.py` or `general_then_author_specific_fine_tuned_model.py`.
3. Check out and click one of the Google Colab links at the top of either file to enter the Google Colab.
4. Make a copy of either Google Colab.
5. Navigate to the files section of the Google Colab copy and copy all the `.txt` files in the `data` folder from the cloned repo into the files section.

<!-- USAGE EXAMPLES -->
## Usage

Navigate to the runtime button dropdown and click the `Run all` button to generate some fairy tale text.

If you want to vary the author used, uncomment the relevant line of code in the author-selection section. (Cell 3 in Google Colab, lines 29-31 in the generated Python files).

If you want to vary the prompts used, change the prompts in the fairy tale text generation section. (Cell 6 in Google Colab).

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/static/v1?label=CONTRIBUTORS&message=3&color=brightgreen
[license-shield]: https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=brightgreen
