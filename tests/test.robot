*** Settings ***
Library   SeleniumLibrary

Suite Setup  Open app in Docker  ${URL}
Suite Teardown  Close browser

*** Variables ***
${URL}                  https://sha-test-app.herokuapp.com
${click_me_btn}         xpath=//button[contains(@class,'default-btn')]
${generate_markup_btn}  id=markup-generation-button

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

*** Keywords ***
Open app in Docker
    [Arguments]  ${url}
    ${chrome_options} =     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}   add_argument    no-sandbox
    ${options}=     Call Method     ${chrome_options}    to_capabilities
    Create Webdriver    Remote   command_executor=http://localhost:8085    desired_capabilities=${options}
    Go to  ${url}