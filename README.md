# How to Run the Code

Follow these detailed steps to set up and run the project.

## 1. Download the mgdb Code
- **Action:** Go to the [mgdb GitHub repository](https://github.com/TayyabaQ27/mgdb.git).
- **Step:** Click on the "Code" button and select "Download ZIP" to download the entire repository to your local machine.
- **Note:** After downloading, extract the ZIP file to a location of your choice on your system.

## 2. Download NCBI Executables
- **Action:** Visit the NCBI BLAST executables download page [here](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/).
- **Step:** Download the appropriate version of the BLAST+ executables for your operating system.
- **Specific Tools:** Ensure that the `blastn` and `blastp` executables are included, as they are required for this project.
- **Environment Variable Setup:**
  1. After downloading and extracting the executables, locate the `bin` folder within the extracted directory.
  2. Add the path to this `bin` folder to your system’s environment variables.
     - On Windows:
       - Right-click on "This PC" or "My Computer" and select "Properties."
       - Click on "Advanced system settings" and then on the "Environment Variables" button.
       - Under "System variables," find the "Path" variable, select it, and click "Edit."
       - Add the path to the `bin` folder and click "OK" to save your changes.
  3. Verify that the executables are accessible by opening a command prompt or terminal and typing `blastn` and `blastp`. They should return a list of options instead of an error.

## 3. Create a New Python Flask Project in Visual Studio
- **Action:** Open Visual Studio on your computer.
- **Step:**
  1. Go to `File > New > Project`.
  2. Search for "Python Flask" in the project templates, and select it.
  3. Name your project and choose a location to save it, then click "Create."
- **Note:** This will set up a basic Python Flask project structure in your specified directory.

## 4. Copy mgdb Code into Your Flask Project
- **Action:** Navigate to the directory where you extracted the `mgdb` code in Step 1.
- **Step:**
  1. Copy all files and folders from the `mgdb` main directory.
  2. Paste these files and folders into the root directory of your newly created Flask project in Visual Studio.
- **Specific Folders:** Ensure that the `databases` and `applications` folders are also copied into the main project directory or change the path in your app.py file. Before running the code, please make sure the all paths in the app.py file are correct.

## 5. Prepare Your Python Environment
- **Action:** In Visual Studio, open the Python environment settings for your project.
- **Step:**
  1. Create or select a Python 3 virtual environment.
  2. Use the terminal or the package manager in Visual Studio to install the necessary libraries:
     - Run `pip install flask` to install Flask.
     - Run `pip install biopython` to install Biopython.
- **Verification:** Confirm that these libraries are installed by checking the list of installed packages in your environment.

## 6. Run Your Solution
- **Action:** After all files are in place and your environment is set up, and paths are correct you can run the project.
- **Step:**
  1. In Visual Studio, go to the "Debug" menu and click "Start Debugging," or simply press `F5`.
  2. The Flask application should start running, and you’ll see output in the console.
- **Note:** The application will be accessible through a web browser at `http://localhost:5000` by default, unless configured otherwise.
