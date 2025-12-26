*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${URL}    https://the-internet.herokuapp.com/dropdown

*** Test Cases ***
Select Dropdown Options
    Open Browser    ${URL}    Chrome

    Select From List By Label       id:dropdown   Option 1
    Sleep    2s

    Select From List By Label       id:dropdown   Option 2
    Sleep    2s

    
    Capture Page Screenshot        dropdown_evidence.png
    Sleep    2s
    Close Browser