from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import random
from faker import Faker

fake = Faker()
test_users = [
    "SELENIUM_TEST",
    "Lois_Lane",
    "Clark_Kent",
    "Jenny_Flex",
]
DELAY = 2


def test_signin(driver):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="' + "/home/signin/" + '"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "username" + '"]').send_keys(test_users[2])
        driver.find_element(by=By.XPATH, value='//input[@name="' + "password" + '"]').send_keys(test_users[2])
        driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()

        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/home/signin/',
            'Attempting to input',
            'Clicking submit',
            'Test Passed!'))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/home/signin/',
            'Attempting to input',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


def test_signin_edit_intro(driver):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="' + "editintro/" + '"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Age" + '"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Age" + '"]').send_keys(random.randrange(1, 100))

        driver.find_element(by=By.XPATH, value='//input[@name="' + "Address" + '"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Address" + '"]').send_keys(fake.address())

        driver.find_element(by=By.XPATH, value='//input[@name="' + "Phone" + '"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Phone" + '"]').send_keys(fake.phone_number())

        driver.find_element(by=By.XPATH, value='//input[@name="' + "Profession" + '"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Profession" + '"]').send_keys(fake.job())

        driver.find_element(by=By.XPATH, value='//input[@name="' + "Status" + '"]').clear()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "Status" + '"]').send_keys(fake.job())

        driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()

        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/editintro/',
            'Attempting to input Age, Address, Phone, Profession, Status.',
            'Clicking submit'))
        # check if info was updated successfully
        try:
            ui_res = driver.find_element(by=By.XPATH,
                                         value='//h2[contains(text(), \'Intro Information Updated!\')]').text
            print('\
            Then: Test Passed -- {}\n' \
                .format(
                ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- {}\n' \
                .format(
                str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/editintro/',
            'Attempting to input Age, Address, Phone, Profession, Status.',
            'Clicking submit',
            'Test Failed! --- ' + str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="' + "/dashboard/" + '"]').click()


def test_signin_add_hobby(driver):
    try:
        sports_lst = ["basketball", "football", "tennis"]
        driver.find_element(by=By.XPATH, value='//a[@href="' + "addhobby/" + '"]').click()
        for i in sports_lst:
            driver.find_element(by=By.XPATH, value='//input[@name="' + "Hobby" + '"]').clear()
            driver.find_element(by=By.XPATH, value='//input[@name="' + "Hobby" + '"]').send_keys(i)
            driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()
            # check if hobby was added successfully
            print('\n\n\
                Feature: {}\n\
                Given conditions: {}\n\
                When: {}' \
                .format(
                'rateer.pythonanywhere.com/dashboard/addhobby/',
                'Attempting to input hobby: ' + i,
                'Clicking submit'))
            try:
                ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Hobby Added!\')]').text
                print('\
                Then: Test Passed -- {}\n' \
                    .format(
                    ui_res))
            except Exception as e:
                print('\
                Then: Test Failed -- {}\n' \
                    .format(
                    str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'rateer.pythonanywhere.com/dashboard/addhobby/',
            'Attempting to input hobby: ' + i,
            'Clicking submit',
            'Test Failed! Details:' + str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="' + "/dashboard/" + '"]').click()


def test_signin_del_hobby(driver):
    try:
        sports_lst = ["basketball", "football", "tennis"]
        driver.find_element(by=By.XPATH, value='//a[@href="' + "delhobby/" + '"]').click()
        for i in sports_lst:
            driver.find_element(by=By.XPATH, value='//input[@name="' + "Hobby" + '"]').clear()
            driver.find_element(by=By.XPATH, value='//input[@name="' + "Hobby" + '"]').send_keys(i)
            driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()
            # check if hobby was del successfully
            print('\n\n\
                Feature: {}\n\
                Given conditions: {}\n\
                When: {}' \
                .format(
                'rateer.pythonanywhere.com/dashboard/delhobby/',
                'Attempting to input hobby: ' + i,
                'Clicking submit'))
            try:
                ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Hobby Deleted!\')]').text
                print('\
                Then: Test Passed -- {}\n' \
                    .format(
                    ui_res))
            except Exception as e:
                print('\
                Then: Test Failed -- {}\n' \
                    .format(
                    str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'rateer.pythonanywhere.com/dashboard/delhobby/',
            'Attempting to input hobby: ' + i,
            'Clicking submit',
            'Test Failed! Details:' + str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="' + "/dashboard/" + '"]').click()


def test_signin_add_edu(driver):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="' + "addeducation/" + '"]').click()
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Degree" + '"]').send_keys(
            "Computer Sciences (Selenium)")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Institute" + '"]').send_keys("ITU University LHR")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_From" + '"]').send_keys("05-05-2020")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Till" + '"]').send_keys("10-10-2022")
        driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/addeducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Certification Added!\')]').text
            print('\
            Then: Test Passed -- {}\n' \
                .format(
                ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- {}\n' \
                .format(
                str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/addeducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="' + "/dashboard/" + '"]').click()


def test_signin_del_edu(driver):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="' + "deleducation/" + '"]').click()
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Degree" + '"]').send_keys(
            "Computer Sciences (Selenium)")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Institute" + '"]').send_keys("ITU University LHR")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_From" + '"]').send_keys("05-05-2020")
        driver.find_element(by=By.XPATH, value='//input[@id="' + "id_Till" + '"]').send_keys("10-10-2022")
        driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/deleducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h2[contains(text(), \'Education Deleted!\')]').text
            print('\
            Then: Test Passed -- {}\n' \
                .format(
                ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- {}\n' \
                .format(
                str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/dashboard/deleducation/',
            'Attempting to input Computer Sciences (Selenium)',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))

    sleep(DELAY)
    driver.find_element(by=By.XPATH, value='//a[@href="' + "/dashboard/" + '"]').click()


def test_signin_find_friend(driver):
    # Find friend
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="' + "/friends/search/" + '"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="' + "queryname" + '"]').send_keys(test_users[3])
        driver.find_element(by=By.XPATH, value='//button[@type="' + "submit" + '"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}' \
            .format(
            'https://rateer.pythonanywhere.com/friends/find/',
            'Attempting to Find Friends',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//b[contains(text(), \'' + test_users[3] + '\')]').text
            print('\
            Then: Test Passed -- User Found -- {}\n' \
                .format(
                ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- User Not Found-- {}\n' \
                .format(
                str(e)))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/friends/find/',
            'Attempting to input data',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


def send_chat(driver):
    # Send chat
    try:
        msg = fake.sentence()
        element = driver.find_element(by=By.XPATH, value='//a[@href="' + "/messenger/chat/" + test_users[3] + '"]')
        driver.execute_script("arguments[0].click();", element)

        driver.find_element(by=By.XPATH, value='//input[@id="' + "MESSAGE" + '"]').send_keys(msg)
        driver.find_element(by=By.XPATH, value='//button[@id="' + "sendBTN" + '"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: Test Passed -- Message Sent -- {}\n' \
            .format(
            'https://rateer.pythonanywhere.com/messenger/chat/' + test_users[3] + '/',
            'Attempting to send chat message',
            'Clicking submit',
            msg))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/messenger/chat/' + test_users[3] + '/',
            'Attempting to send chat message',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


def view_profile(driver):
    try:
        msg = fake.sentence()
        element = driver.find_element(by=By.XPATH, value='//a[@href="' + "/friends/" + test_users[3] + '/"]')
        driver.execute_script("arguments[0].click();", element)

        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: Test Passed\n' \
            .format(
            'https://rateer.pythonanywhere.com/friends/' + test_users[3] + '/',
            'Attempting to find friend',
            'Clicking submit', ))

    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            'https://rateer.pythonanywhere.com/friends/' + test_users[3] + '/',
            'Attempting to find friend',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


def friend_request(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value='//a[@href="' + "/friends/friendrequest/" + test_users[3] + '/"]').click()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: Test Passed\n' \
            .format(
            '/friends/friendrequest/' + test_users[3] + '/',
            'Attempting to send friend request',
            'Clicking submit', ))

    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            '/friends/friendrequest/' + test_users[3] + '/',
            'Attempting to send friend request',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))
    pass


def rate(driver):
    try:
        element = driver.find_element(by=By.XPATH, value='//a[@href="' + "/friends/rate/" + test_users[3] + '/' + str(
            random.randint(1, 5)) + '/"]')
        driver.execute_script("arguments[0].click();", element)

        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: Test Passed\n' \
            .format(
            '/friends/rate/' + test_users[3] + '/[]/',
            'Attempting to rate friend',
            'Clicking submit', ))

    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}' \
            .format(
            '/friends/rate/' + test_users[3] + '/[]/',
            'Attempting to rate friend',
            'Clicking submit',
            'Test Failed! Details:' + str(e)))


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://rateer.pythonanywhere.com/')
        driver.maximize_window()
    except Exception as e:
        print(str(e))
        exit(1)

    print("Running Tests...")

    print("Starting test [Sign In]")
    test_signin(driver)
    print("Finished test [Sign In]")
    sleep(DELAY)

    print("Starting test [Edit Intro]")
    test_signin_edit_intro(driver)
    print("Finished test [Edit Intro]")
    sleep(DELAY)

    print("Starting test [Add Hobby]")
    test_signin_add_hobby(driver)
    print("Finished test [Add Hobby]")
    sleep(DELAY)

    print("Starting test [Remove Hobby]")
    test_signin_del_hobby(driver)
    print("Finished test [Remove Hobby]")
    sleep(DELAY)

    print("Starting test [Add Education]")
    test_signin_add_edu(driver)
    print("Finished test [Add Education]")
    sleep(DELAY)

    print("Starting test [Del Education]")
    test_signin_del_edu(driver)
    print("Finished test [Del Education]")
    sleep(DELAY)

    print("Starting test [Find Friends]")
    test_signin_find_friend(driver)
    print("Finished test [Find Friends]")
    sleep(DELAY)

    print("Starting test [send chat]")
    test_signin_find_friend(driver)
    send_chat(driver)
    print("Finished test [send chat]")
    sleep(DELAY)

    print("Starting test [View Profile]")
    test_signin_find_friend(driver)
    view_profile(driver)
    print("Finished test [View Profile]")
    sleep(DELAY)

    print("Starting test [Friend Request]")
    test_signin_find_friend(driver)
    view_profile(driver)
    friend_request(driver)
    print("Finished test [Friend Request]")
    sleep(DELAY)

    print("Starting test [Rate]")
    test_signin_find_friend(driver)
    view_profile(driver)
    rate(driver)
    print("Finished test [Rate]")
    sleep(DELAY)

    # Add posts feature testing
    # Parameterize Functions and modularize scripts
    # Push to repo
    # store results in file

    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    driver.quit()
