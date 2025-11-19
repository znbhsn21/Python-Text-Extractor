# Keyword Extractor 🔑

A simple Python script to extract the most frequent keywords from a text file. This project provides a straightforward solution for text analysis, allowing users to quickly identify the key themes and topics within a document. It's designed to be easily integrated into other projects requiring text summarization or keyword identification.

🚀 **Key Features**

*   **Keyword Extraction:** Identifies and extracts the most frequent keywords from a given text file.
*   **Text Cleaning:** Removes punctuation and converts text to lowercase for accurate analysis.
*   **Customizable:** Allows users to specify the number of keywords to extract.
*   **File Handling:** Checks for file existence and reads files with UTF-8 encoding.
*   **Easy Integration:** Can be easily integrated into other Python projects.
*   **Sample File Creation:** Automatically creates a sample "test.txt" file if one doesn't exist.

🛠️ **Tech Stack**

*   **Language:** Python 3.x
*   **Modules:**
    *   `os` (for file system operations)
    *   `string` (for punctuation removal)
    *   `collections` (`Counter` for word frequency counting)

📦 **Getting Started**

### Prerequisites

*   Python 3.6 or higher

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  No additional packages need to be installed as all dependencies are part of the Python standard library.

### Running Locally

1.  Navigate to the project directory in your terminal.
2.  Run the script:

    ```bash
    python main.py
    ```

    This will create a `test.txt` file (if it doesn't exist) and print the top 5 keywords from the file. You can modify the number of keywords extracted by changing the `num_of_keywords` argument in the `main.py` file.

📂 **Project Structure**

```
.
├── main.py
└── test.txt
```

📸 **Screenshots**

<div align="center">
  <div style="display: inline-block; text-align: center; margin: 0 15px;">
    <p><strong>Test File</strong></p>
    <img src="screenshots\Screenshot 2025-11-19 202334.png" alt="Screenshot showing test file" width="400"/>
  </div>

  <div style="display: inline-block; text-align: center; margin: 0 15px;">
    <p><strong>Keywords Extracted Using Script</strong></p>
    <img src="screenshots\Screenshot 2025-11-19 202400.png" alt="Screenshot showing the fkeywords after running script" width="400"/>
  </div>
</div>

🤝 **Contributing**

Contributions are welcome! Please feel free to submit pull requests with bug fixes, improvements, or new features.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to your fork.
5.  Submit a pull request.

📬 **Contact**

If you have any questions or suggestions, feel free to contact me at zenabadnan10@gmail.com

💖 **Thanks**

Thank you for checking out this project! I hope it's helpful for your text analysis needs.


