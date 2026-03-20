<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT TITLE CARD -->
<br />
<div align="center">
  <h3 align="center">FGC Match Control</h3>

  <p align="center">
    A reworked FGC overlay controller for general FGC tournament streaming needs.
    <br />
    IN PROGRESS
    <br />
    <br />
    <a href="https://github.com/barnesrd/fgc-match-control/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/barnesrd/fgc-match-control/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Based on work done for the Persona 4 Arena Ultimax community, this reworked program aims to provide the framework for a fully moddable autofill experience via json files. This project is fully built in Python 3.10+ and utilizes Qt bindings from the PySide6 library. This allows for compilation to Linux, Windows and Mac executables, removing the need for translation layers (as was needed in the previous version).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
 - [![P6Side6][PySide6-shield]][PySide6-url] <b>PySide6</b> - Qt bindings for Python
 - [![Ruff][Ruff-shield]][Ruff-url] <b>Ruff</b> - Code linter and style enforcer

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can either download compiled executables from this project's releases directory or clone this repository for local use.

### Releases

Navigate to the [Releases](https://github.com/barnesrd/fgc-match-control/releases) section of this repository and download the latest executable for your operating system.


### Prerequisites

If you want to clone this repository onto your machine, you will need the following prerequisites:
* [Python 3.10+](https://www.python.org/downloads/)

That's it!

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/barnesrd/fgc-match-control.git
   ```
2. (Optional) Create a new virtual environment for this project
   
   Create the environment.
   ```
   python -m venv /path/to/new/virtual/environment
   ```
   Activate the new environment. <b>(```<venv>``` must be replaced by the path to the directory containing the virtual environment)</b>
   | Platform | Shell      | Command to activate venv                  |
   | -------- | --------   | ----------------------------------------- |
   | POSIX    | bash/zsh   | ```$ source <venv>/bin/activate```        |
   | POSIX    | fish       | ```$ source <venv>/bin/activate.fish```   |
   | POSIX    | csh/txsh   | ```$ source <venv>/bin/activate.csh```    |
   | POSIX    | pwsh       | ```$ <venv>/bin/Activate.ps1```           |
   | Windows  | cmd.exe    | ```C:\> <venv>\Scripts\activate.bat```    |
   | Windows  | PowerShell | ```PS C:\> <venv>\Scripts\Activate.ps1``` |
3. Install packages with pip
   ```sh
   pip install -r requirements.txt
   ```
4. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github-username/repository-name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```sh
python main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap to version 1.0

- [x] Player Controls
- [x] Commentator Controls
- [x] Match Title Controls
- [ ] Crewbattle Controls (Delayed)
  - [ ] Add players via button
  - [ ] Autofill teams by team title if saved
  - [ ] Add quality of life toggles (Update on edit, clear overlay on "clear", etc.)
- [ ] Add Menu Bar functionality
  - [ ] Create options and preferences menu
  - [ ] Create custom profile support
  - [ ] Create game theme creation window
  - [ ] Add information section
  - [ ] Create basic tutorials in help menu
- [ ] Refine User Experience


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions or suggestions are greatly appreciated! If you have a suggestion that would improve this project, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement". 

It is reccommended that any pushes follow code style guidelines enforced by [Ruff].

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AdditionalFeature`)
3. Commit your Changes (`git commit -m 'Add some AdditionalFeature'`)
4. Push to the Branch (`git push origin feature/AdditionalFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Contributors:

<a href="https://github.com/barnesrd/fgc-match-control/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=barnesrd/fgc-match-control" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the MIT license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/barnesrd/fgc-match-control.svg?style=for-the-badge
[contributors-url]: https://github.com/barnesrd/fgc-match-control/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/barnesrd/fgc-match-control.svg?style=for-the-badge
[forks-url]: https://github.com/barnesrd/fgc-match-control/network/members
[stars-shield]: https://img.shields.io/github/stars/barnesrd/fgc-match-control.svg?style=for-the-badge
[stars-url]: https://github.com/barnesrd/fgc-match-control/stargazers
[issues-shield]: https://img.shields.io/github/issues/barnesrd/fgc-match-control.svg?style=for-the-badge
[issues-url]: https://github.com/barnesrd/fgc-match-control/issues
[license-shield]: https://img.shields.io/github/license/barnesrd/fgc-match-control.svg?style=for-the-badge
[license-url]: https://github.com/barnesrd/fgc-match-control/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ryan-barnes-houston
[PySide6-shield]: https://img.shields.io/badge/Qt-2CDE85?logo=Qt&logoColor=fff
[PySide6-url]: https://doc.qt.io/qtforpython-6.9/
[Ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[Ruff-url]: https://docs.astral.sh/ruff/
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
