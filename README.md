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

The goal of the project is to create a text generation model that will learn from existing fairy tales and auto-generate new and plausible fairy tale texts

### Built With

* GPT-2

<!-- INSTALLATION -->
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lmu-mandy/project-breadcrumbs.git
   ```
2. Navigate to either author_specific_fine_tuned_model.py or
general_then_author_specific_fine_tuned_model.py
3. Check out and click one of the google collab links at the top of either file to enter the google collab
4. Make a copy of either google collab
5. Navigate to the files section of copy google collab and copy all the txt files from data folder from the cloned repo and insert them into the files section of the copied google collab

<!-- USAGE EXAMPLES -->
## Usage

Navigate to the runtime button dropdown and click the run all button to generate some fairy tail text.

If you want to vary the authors used, uncomment the commented lines of code in the preprocessing section.

If you want to vary the prompts used, change the prompts in the fairy tale text generation section.

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/static/v1?label=CONTRIBUTORS&message=3&color=brightgreen
[license-shield]: https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=brightgreen
