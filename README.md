# FileTransformerAI

FileTransformerAI is a Python project that utilizes Docker to transform files. It allows you to convert files from one extension to another or perform more sophisticated transformations using AI, such as translation, audio transcription, or text-to-speech.

## Getting Started

To get started with FileTransformerAI, follow these steps:

1. Clone the repository to your local system by running the following command in your terminal:

    ```
    git clone https://github.com/coding-samu/FileTransformerAI.git
    ```

2. Make sure you have Docker installed on your system.

3. Navigate to the cloned repository in your terminal.

4. Start the Docker container by running the following command:

    ```
    docker-compose up --build
    ```

5. Once the Docker container is running, open a terminal within the Docker environment.

6. Execute the following command to start the program:

    ```
    python src/main.py
    ```

## Usage

- Place the files you want to convert inside the "input_files" folder.
- The converted output files will be saved in the "output_files" folder.

Feel free to explore the various transformation options available in FileTransformerAI.

## Languages

When specifying the language, please use the standard format. For example, Italian is represented as "it", English as "en", Spanish as "es", and so on.
