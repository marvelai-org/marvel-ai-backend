from app.features.notes_generator.core import executor
from unittest.mock import patch


"""if there is an error of file not found while trying to test directly with
    pytest test_core.py, please use this path👇🏻
    'PYTHONPATH=./ pytest app/features/notes_generator/tests/test_core.py' """

#Test cases for the executor function

def test_executor_text_input_valid():
    """Test executor with valid text input."""
    result = executor(
        input_type='text',
        input_content="Photosynthesis is a process used by plants.",
        focus_topic="Summarize the key steps of photosynthesis",
        output_structure='bullet',
        export_format='txt'
    )
    assert result["status"] == "success"
    assert "file_path" in result

@patch('app.features.notes_generator.tools.extract_text_from_file') # Mock the extract_text_from_file function
def test_executor_file_input_valid(mock_extract):

    """
    Test extracting text from a file using a mocked version of the extract_text_from_file function.

    This test ensures that we can simulate the behavior of the extract_text_from_file function without
    actually reading from a file. We mock the function to return predefined content and verify that the
    logic of the function consuming it behaves as expected.

    Args:
        mock_extract (MagicMock): Mocked version of the extract_text_from_file function.
    """
    # Ensure the mock returns a simple, valid text string, also the file_path is a dummy file path, though the file is present in the directory to avoid FileNotFoundError
    # Ensure the mock returns a simple, valid text string
    mock_extract.return_value = "Plants convert sunlight into energy"
    result = executor(
        input_type='file',
        file_path="dummy.pdf",
        focus_topic="Photosynthesis steps",
        output_structure='paragraph',
        export_format='docx'
    )
    assert result["status"] == "success"
    assert "file_path" in result

def test_executor_missing_input():
    """Test executor with missing inputs."""
    result = executor(input_type='text', input_content=None)
    assert result["status"] == "error"

def test_executor_invalid_file_type():
    """Test executor with unsupported file type."""
    result = executor(
        input_type='file',
        file_path="unsupported.xyz",
        focus_topic="Photosynthesis steps",
        output_structure='paragraph',
        export_format='docx'
    )
    assert result["status"] == "error"
    assert "Unsupported file type for file" in result["message"]

@patch('app.features.notes_generator.tools.extract_text_from_url')
def test_executor_url_input_valid(mock_extract):
    """Test executor with valid URL input."""
    mock_extract.return_value = "Sunlight absorbed by plants for photosynthesis."
    result = executor(
        input_type='url',
        input_content="fFlG9waFfJE", #This is a valid youtube video id from (https://www.youtube.com/watch?v=fFlG9waFfJE), you can replace it with any valid youtube video id
        focus_topic="Photosynthesis steps",
        output_structure='table',
        export_format='pdf'
    )
    assert result["status"] == "success"
    assert "file_path" in result