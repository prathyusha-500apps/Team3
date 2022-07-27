from unicodedata import name
from behave import *
from urllib.parse import urljoin
from selenium.webdriver.common.action_chains import ActionChains
from behave_webdriver.steps import *
from apps.lib.automation_base import Base
from apps.finder.features.steps.locators import Locators
from apps.lib.core_steps import *


elements = Locators()

base_methods = Base()


@then('I verified the count of the emails "{count}" using the element "{element}"')
def domain_validations(context, count, element):
    emails = context.behave_driver.find_elements_by_xpath(element)
    assert len(emails) == int(count)


@when('I scroll the form using infinity scroll')
def scroll_in_the_form(context):
    base_methods.move_to_element(context, elements.move_to_25th_row)


@when('I click on create list "{text}" button')
def click_create_list_button(context, text):
    base_methods.click_element(
        context, f"//div[@id='createListForm']//fieldset[@id='listname']//div//button[@type='submit'][normalize-space()='{text}']")


@then('I expect error message as "{text}"')
def verify_error_messages(context, text):
    base_methods.element_visible(
        context, f"//small[normalize-space()='{text}']")


@then('I expect error message "{text}" is visible')
def verify_error_messages(context, text):
    base_methods.element_visible(
        context, f"//span[contains(@class,'text-danger mt-1 small')]")


@when('I click on "{text}" button of the list "{listname}"')
def delete_list(context, text, listname):
    base_methods.action_click(
        context, f"//a[contains(text(),'{listname}')]//ancestor::tr//descendant::td[3]//span[@title='{text}']")


@then('I expect the free domain error message as "{text}"')
def verify_free_domain_error_message(context, text):
    base_methods.element_visible(context, f"//td[normalize-space()='{text}']")

@when('I click on element "{text}"')
def domain_verify(context, text):
    base_methods.action_click(
        context, f"//tbody/tr[1]/td[3]/div[1]/div[1]/a[text()='Verify']")

@when('I click on the button text "{text}"')
def add_to_crm(context, text):
    base_methods.action_click(
        context, f"//p[@role='button']")

@when('I click on the button having text "{text}"')
def save_crm(context, text):
    base_methods.action_click(
        context, f"//button[@type='submit'][normalize-space()='Save']")

@when('I click on "{text}" icon in contacts')
def step_impl(context, text):
    base_methods.action_click(
        context, f"//h3[contains(text(),'Contacts')]//following::span[@title='{text}']")

@when('I select category "{attr}" "{text}" in domainsearch')
def click_on_drop_down(context, attr, text):
    base_methods.select_option_by(context, attr, text, f"//select[@class='mr-2 select-option custom-select custom-select-sm']")

@when('I add "{text}" into search field "{header}"')
def add_input(context, text, header):
    base_methods.input_text_locator(
        context, text, f"//div[contains(text(),'{header}')]//preceding::input[@placeholder='Search'][1]")







   
# @when('I add "{text}" into the placeholder "{placeholder}"')
# def step_impl(context, text, placeholder):
#    base_methods.input_data_with_contains_placeholder(context, text, placeholder)

# @then('I expect that the element contains text "{text}" is visible')
# def step_impl(context, text):
#     base_methods.elements_visible(
#         context,f"//p[text()='prathyusha.siripothu@500apps.com']")


@when('I add "{text}" using placeholder "{placeholder}"')
def step_impl(context, text, placeholder):
    base_methods.input_data_with_contains_placeholder(context, text,placeholder)


@when('I add "{text}" into the inputfield using the id "{id_value}"')
def input_data_with_id_value(context, text, id_value):
    base_methods.input_data_with_id(context, text, id_value)

@when('I click on the button using the text "{text}"')
def click_button(context, text):
    base_methods.click_button_text(context, text)


@then('I expect that the element contains text "{text}" is vissible')
def step_impl(context, text):
    base_methods.element_visible(
        context, f"//*[text()='{text}']")

@when('I click on textlink "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//*[text()='{text}']")

@when('I click on linktext "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//*[text()='{text}']")

@when('I pass data "{text}" into list name field in "{module_name}" Add to List popup')
def step_impl(context, text, module_name):
    base_methods.input_text_locator(context, text, f"//div[@id='modal-add-to-list-{module_name}___BV_modal_body_']//following::input" )


@when('I click on button using text "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//button[text()='{text}']")

@then('I expect that  the element contains text "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//*[text()='{text}']")

@then('I expect that the element contains text "{text}" is visible')
def step_impl(context, text):
    base_methods.element_visible(context, f"//*[text()='{text}']")

@when('I click on the "{text}" icon in contacts')
def step_impl(context, text):
    base_methods.click_element(context, f"//h3[contains(text(),'Contacts')]//following::span[@title='{text}']")

@when('I click on the "{title}" icon in a row')
def step_impl(context, title):
    base_methods.click_element(context, f"//tbody/tr[1]//child::span[@title='{title}']")

@then('I expect that the element with text "{text}" does not exist "{option}"')
def step_impl(context, text, option):
    base_methods.verify_element_exists(context,f"//*[normalize-space()='{text}']", option)

@when('I click on element contains text "{text}"')
def step_impl(context, text):
    base_methods.action_click(context, f"//*[text()='{text}']")

@when('I upload file "{filename}" in "{app_name}" app using class "{class_name}"')
def upload_file(context, filename, class_name, app_name):
    base_methods.upload_files(
        context, filename, f"//input[contains(@class,'{class_name}')]", app_name)

@when('I click on button "{text}"')
def step_impl(context, text):
    base_methods.click_element(context, f"//span[text()='Reset']")

when('I click on the button tex t "{app_name}"')
def step_impl(context, app_name):
    base_methods.click_element(context, f"//h5[text()='{app_name}']")

@when(u'I wait for element "{element}" with in "{time}" seconds')
def step_impl(context, element, time):
    base_methods.explicit_wait(
        context, time, element)