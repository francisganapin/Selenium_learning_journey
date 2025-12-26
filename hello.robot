*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.python.org
${BROWSER}  Chrome

*** Test Cases ***
Open Python Website
    [Documentation]    Opens the Python website and checks the title.
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Welcome to Python.org
    Sleep    5s
    Close Browser