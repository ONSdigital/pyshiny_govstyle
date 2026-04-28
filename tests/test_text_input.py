"""Unit tests for text_input component."""

import pytest  # noqa: F401

from tests.conftest import Case, parametrize_cases

from pyshinygovstyle.ui.text_input import text_input


class TestTextInput:
    """Test text_input component."""

    @parametrize_cases(
        Case("basic",
               input_id="event_name",
               label="What is the name of the event?",
             width=None,
             prefix=None,
             suffix=None,
             ),
        Case("with width",
               input_id="event_name",
               label="What is the name of the event?",
             width=10,
             prefix=None,
             suffix=None,
             ),
        Case("with prefix",
               input_id="event_name",
               label="What is the name of the event?",
             width=10,
               prefix="Prefix",
             suffix=None,
             ),
        Case("with suffix",
               input_id="event_name",
               label="What is the name of the event?",
             width=10,
             prefix=None,
               suffix="Suffix",
             ),
        Case("with prefix and suffix",
               input_id="event_name",
               label="What is the name of the event?",
             width=10,
               prefix="Prefix",
               suffix="Suffix",
             ),
    )

    def test_text_input_renders_basic(self, input_id, label, width, prefix, suffix):
        """Test the basic rendering of the text_input component.

        Args:
            input_id (str): The ID of the input element.
            label (str): The label for the input element.
            width (int, optional): The width of the input element.
            prefix (str, optional): The prefix for the input element.
            suffix (str, optional): The suffix for the input element.
        """
        html = text_input(input_id, label, width=width, prefix=prefix, suffix=suffix)
        traverse_children = 0
        assert input_id == str(html.children[traverse_children].attrs["for"])
        assert label == str(html.children[traverse_children].children[0])
        traverse_children += 1
        if prefix is not None and suffix is not None:
            assert html.children[traverse_children].attrs["class"] == "govuk-input__wrapper"
            # traverse_2 = 0
            # if prefix is not None:
            #     assert prefix == str(html.children[traverse_children].children[traverse_2]
            #       .children[0])
            #     traverse_2 += 1
            # assert  input_id == str(html.children[traverse_children].children[traverse_2]
            #       .attrs["id"])
            # if suffix is not None:
            #     assert suffix == str(html.children[traverse_children].children[traverse_2]
            #       .children[0])
        else:
            self.main_textbox_assertions(html.children[traverse_children], width, input_id)

    def main_textbox_assertions(self, main_textbox, width, input_id):
        """Perform assertions for the main textbox element.

        Args:
            main_textbox (Tag): The main textbox element to assert against.
            width (int, optional): The width of the input element.
            input_id (str): The ID of the input element.
        """
        assert main_textbox.name == "input"
        assert main_textbox.attrs["type"] == "text"
        assert main_textbox.attrs["id"] == input_id
        assert main_textbox.attrs["name"] == input_id
        assert "govuk-input" in main_textbox.attrs["class"]
        if width is not None:
            assert f"govuk-input--width-{width}" in main_textbox.attrs["class"]


        # assert against last part of class
        #assert ["govuk-label-wrapper", "govuk-input"] == [child.attrs['class'].split()[-1] for
        #   child in html.children]
        # example_html = """
        # <div class="govuk-form-group">
        #     <h1 class="govuk-label-wrapper">
        #         <label class="govuk-label govuk-label--l" for="event_name">
        #         What is the name of the event?
        #         </label>
        #     </h1>
        #     <input class="govuk-input" id="event_name" name="eventName" type="text">
        #     </div>
        # """
        #assert str(html).strip() == example_html.strip()


# def test_text_input_with_placeholder():
#     html = text_input('id2', 'Label', placeholder='Type here')
#     assert 'placeholder="Type here"' in html

# def test_text_input_with_value():
#     html = text_input('id3', 'Label', value='default')
#     assert 'value="default"' in html

# def test_text_input_with_additional_classes():
#     html = text_input('id4', 'Label', classes='extra-class')
#     assert 'extra-class' in html

# def test_text_input_raises_on_missing_id():
#     with pytest.raises(TypeError):
#         text_input(label='No ID')
