#13.

# How to Run `main.py`

To run the `main.py` script, follow these steps:

1. **Navigate to the Project Directory**:
    Open your terminal and navigate to the directory where `main.py` is located. For example:
    ```sh
    cd /home/user/AppProject
    ```

2. **Ensure Python is Installed**:
    Make sure you have Python installed on your system. You can check this by running:
    ```sh
    python --version
    ```
    If Python is not installed, download and install it from [python.org](https://www.python.org/) or run:

    **On Windows:**
    ```sh
    winget install Python.Python.3
    ```
    **On Linux:**
    ```sh
     sudo apt-get install -y python3
    ```
    **On MACOS:**
    ```sh
     brew install python
    ```

3. **Install Required Dependencies**:
    If your project has dependencies, install them using `pip`. Typically, dependencies are listed in a `requirements.txt` file. Run:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Script**:
    Execute the `main.py` script by running:
    ```sh
    python main.py
    ```

That's it! Your `main.py` script should now be running.