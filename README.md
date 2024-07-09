# Squad Busters Computer Vision Project

## Overview

This project aims to utilize computer vision techniques on the Supercell mobile game, **Squad Busters**. The primary objective is to identify important objects such as chests and boxes (and coins) within the game. Given the game's 3D nature, achieving a perfect match for object is quite impossible.

## Getting Started

### Prerequisites

- [scrcpy](https://github.com/Genymobile/scrcpy): A tool to display and control Android devices from your computer.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/squad-busters-vision.git
    cd squad-busters-vision
    ```

2. Install necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up scrcpy to access your Android phone. 

### Usage

1. Run the object detection script:
    ```bash
    python chest_reco_upgrade.py
    ```

2. To get the coordinates of any pixel on the screen, use:
    ```bash
    python mouse_coord.py
    ```

### Future Enhancements

- **Control via Computer**: There are plans to control the game from the computer using scrcpy if I figure out how to sprint while moving with only 1 mouse.
- **Improved Screenshots**: Cleaner screenshots will be taken to achieve better detection results.

---

Feel free to improve the project and share your feedback!
