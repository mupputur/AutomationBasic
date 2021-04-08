from selenium.webdriver.common.by import By


class LPraForm():
    first_name =(By.NAME, "firstname")
    last_name = (By.NAME,"lastname")
    gender = (By.ID,"sex-0")
    exp = (By.ID,"exp-3")
    date = (By.ID,"datepicker")
    pro =(By.XPATH, "//*[@id='post-body-3077692503353518311']/div/div/div[21]/label")
    tool1 = (By.ID,"tool-0")
    tool2 = (By.ID,"tool-2")
    continent = (By.ID,"continents")
    cmds = (By.XPATH,"selenium_commands")
    photo = (By.ID,"photo")
    submit = (By.ID,"submit")




