*** Settings ***
Library   src\\HealeniumLibrary.py

Suite Setup  Open Selfhealing Browser   ${url}
Suite Teardown  Close browser

*** Variables ***
${url}                  https://sha-test-app.herokuapp.com
${click_me_btn}         //button[contains(@class,'default-btn')]
${generate_markup_btn}  //*[@id='markup-generation-button']

*** Test Cases ***
Click me button test
    [Documentation]  Simple smoke test that should always pass
    Click Element   ${click_me_btn}
    Handle Alert    action=ACCEPT

Click me button test with healing
    [Documentation]  Test the selfhealing functionality of Healenium
    Click Element   ${click_me_btn}
    Handle Alert    action=ACCEPT
    Click Element   ${generate_markup_btn}  # generate new layout -> locators going to change
    Click Element   ${click_me_btn}  # should be healed
    Handle Alert    action=ACCEPT