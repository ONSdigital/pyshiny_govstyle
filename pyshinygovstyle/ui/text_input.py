"""
text_input component created following GOV.UK design system.

Implemented by using Shiny for Python's input_text component as a base.

Reference: https://design-system.service.gov.uk/components/text-input/
"""

from shiny import ui


def text_input(
    input_id,
    label,
    value="",
    width=None,
    placeholder=None,
    error=False,
    error_message=None,
    prefix=None,
    suffix=None,
) -> ui.Tag:
    """Create a text input HTML component.

    Args:
        input_id (str): id of the input element
        label (str): label to appear above the input element
        value (str, optional): default value of the input element. Defaults to "".
        width (int, optional): width of the input element (in characters).
                               Defaults to None.
        placeholder (str, optional): placeholder text for the input element.
                                     Defaults to None.
        error (bool, optional): whether the input element has an error.
                                Defaults to False.
        error_message (str, optional): error message to display. Defaults to None.
        prefix (str, optional): prefix text to appear before the input element.
                                Defaults to None.
        suffix (str, optional): suffix text to appear after the input element.
                                Defaults to None.

    Returns
    -------
        ui.Tag: a Shiny UI tag representing the text input component
    """
    class_build = "govuk-input"
    if width is not None:
        class_build += f" govuk-input--width-{width}"

    textbox = ui.input_text(
        input_id,
        label,
        value=value,
        width=width,
        placeholder=placeholder,
    )

    if textbox.children[1].has_class("form-control"):
        textbox.children[1].remove_class("form-control")
    textbox.children[1].add_class(class_build)

    parts_list = []

    label_element = ui.tags.label(label, class_="govuk-label", for_=input_id)

    parts_list.append(label_element)
    if error:
        error_message_element = ui.div(
            error_message, class_="govuk-error-message", id=f"{input_id}-error",
        )
        parts_list.append(error_message_element)
        textbox.children[1].attrs["aria-describedby"] = f"{input_id}-error"
        textbox.children[1].add_class("govuk-input--error")
    if prefix is None and suffix is None:
        parts_list.append(textbox.children[1])
    else:
        textbox_wrapper = []

        if prefix is not None:
            textbox_wrapper.append(
                ui.div(prefix, class_="govuk-input__prefix", aria_hidden="true"),
            )
        textbox_wrapper.append(textbox.children[1])
        if suffix is not None:
            textbox_wrapper.append(
                ui.div(suffix, class_="govuk-input__suffix", aria_hidden="true"),
            )
        parts_list.append(ui.div(*textbox_wrapper, class_="govuk-input__wrapper"))

    full_component_class = "govuk-form-group"
    if error:
        full_component_class += " govuk-form-group--error"
    full_component = ui.div(
        ui.TagList(
            *parts_list,
        ),
        class_=full_component_class,
        id=f"{input_id}_div",
    )

    return full_component
