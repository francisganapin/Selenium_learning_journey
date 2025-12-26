*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${LOGIN_URL}    https://the-internet.herokuapp.com/login
${USERNAME}     tomsmith
${PASSWORD}     SuperSecretPassword!

*** Test Case ***
Login To Secure Area
    [Documentation]  Logs into the internet herokuapp

    Open Browser    ${LOGIN_URL}    Chrome

    Input Text      id:username     ${USERNAME}

    Input Password  id:password     ${PASSWORD}

    Click Button    css:button.radius

    Wait Until Page Contains    Secure Area

    Sleep    5s

    Close Browser