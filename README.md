# 🎵 Python CLI Music Player

![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-blue)
![Language](https://img.shields.io/badge/Language-Python_3-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight, terminal-based music player built with Python. This project demonstrates modular system design, separating data handling, UI rendering, and playback logic into distinct components.

## 📖 Table of Contents
- [About](#about)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Usage](#installation--usage)
- [Controls](#controls)
- [Future Roadmap](#future-roadmap)

## 🧐 About
This application is a Command Line Interface (CLI) tool that scans local directories for audio files and provides an interactive playback session. It utilizes the `pygame` library for audio processing and the `os` library for file system navigation.

## 🏗 System Architecture
The project follows a modular design pattern to ensure scalability and maintainability:

```text
MusicPlayer/
│
├── main.py            # Entry point & Main Event Loop (Director)
├── music/             # Directory for .mp3 assets
└── README.md          # Project Documentation
````

**Core Modules:**

1.  **Data Handler:** Scans directories and filters valid `.mp3` files.
2.  **UI Renderer:** A dynamic text-based interface that refreshes based on state.
3.  **Playback Engine:** Handles audio states (Loading, Playing, Stopping).
4.  **Session Controller:** A dedicated state machine for user input during playback (Pause, Resume, Volume).

## 🚀 Features

  * **Dynamic File Loading:** Automatically detects `.mp3` files in the source folder.
  * **Interactive Menu:** Clean CLI interface for song selection.
  * **Playback State Control:** Pause, Resume, and Stop functionality.
  * **Volume Control:** Dynamic volume adjustment with input validation (0.0 - 1.0).
  * **Input Sanitization:** Handles invalid inputs gracefully without crashing.

## ⚙️ Prerequisites

  * Python 3.x
  * `pip` (Python Package Installer)

## 📥 Installation & Usage

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/yourusername/music-player.git](https://github.com/yourusername/music-player.git)
    cd music-player
    ```

2.  **Install Dependencies**

    ```bash
    pip install pygame
    ```

3.  **Add Music**

      * Create a folder named `music` in the root directory.
      * Add your `.mp3` files into this folder.

4.  **Run the Application**

    ```bash
    python main.py
    ```

## 🎮 Controls

Once a song is playing, the following commands are available:

| Key | Action | Description |
| :--- | :--- | :--- |
| **P** | Pause | Pauses the current track. |
| **R** | Resume | Resumes playback from the paused timestamp. |
| **V** | Volume | Opens the volume configuration prompt. |
| **S** | Stop | Stops the track and returns to the Main Menu. |

## 🗺 Future Roadmap

We are tracking upcoming features via GitHub Issues. Planned updates include:

  * [ ] **Next/Previous Navigation:** Functionality to skip tracks without returning to the menu.
  * [ ] **Metadata Display:** Displaying Artist/Title using ID3 tags instead of filenames.
  * [ ] **Favorites Playlist:** Persistence layer to save preferred songs.
  * [ ] **TUI Migration:** Moving from a linear CLI to a curses-based Text User Interface.

-----

### 🤝 Contributing

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewFeature`)
3.  Commit your Changes (`git commit -m 'Add some NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request
