*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${URL}   https://www.python.org
${BROWSER}  Chrome



*** Test Cases ***
Search for Pycon
    [Documentation]     Goes to Python.org and searches for 'pycon'

    Open Browser  ${URL}  ${BROWSER}

    Input Text  name:q  pycon

    Press Keys  name:q  RETURN

    Wait Until Page Contains  PyCon     timeout=10s

    Close Browser